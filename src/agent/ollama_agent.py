import json
from openai import OpenAI
from src.agent.weather_tool import get_daily_forecast, WEATHER_TOOL_DEFINITION
from src.agent.settings import LLMConfig

WEATHER_PROMPT = ("Você é um assistente meteorológico."
                  "Se receber a palavra latitude seguido de um número, "
                  "e a palavra longitude seguido de um número,"
                  "e a palavra dias seguido de um número na pergunta, "
                  "você DEVE responder APENAS com a chamada de função get_daily_forecast. Não escreva explicações."
                  "Não tente adivinhar ou inventar previsões. "
                  "Se não tiver os números das coordenadas, peça educadamente para o usuário fornecê-las.")

SYSTEM_PROMPT = ("Você é um assistente meteorológico."
                 "Você receberá dados meteorológicos em formato JSON. "
                 "Use esses dados e apresente para cada dia SEPARADAMENTE:"
                 "- A temperatura máxima (temperature_2m_max);"
                 "- A temperature mínima (temperature_2m_min);"
                 "- A precipitação de chuva naquele dia (precipitation_sum)."
                 "Se não receber dados meteorológicos, peça educadamente "
                 "para o usuário fornecer as coordenadas (latitude, longitude) e dias necessários "
                 "para que você possa fornecer a previsão do tempo.")


class OllamaAgent:
    def __init__(self, cfg: LLMConfig):
        self.client = OpenAI(base_url=cfg.base_url, api_key=cfg.api_key)
        self.cfg = cfg
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
        self.weather_messages = [
            {
                "role": "system",
                "content": WEATHER_PROMPT
            }
        ]

    def chat(self, user_input: str):
        user_message = {"role": "user", "content": user_input}
        weather_input = self.weather_messages + [user_message]

        # Primeira parte: identificar se precisa de uma ferramenta
        response = self.client.chat.completions.create(
            model=self.cfg.model,
            messages=weather_input,
            tools=[WEATHER_TOOL_DEFINITION],
            temperature=self.cfg.temperature  # Estabilidade máxima para modelos pequenos
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            self.messages.append({"role": "user", "content": user_input})
            for tool_call in msg.tool_calls:
                args = json.loads(tool_call.function.arguments)
                params = args.get('parameters', args)  # Suporte para ambos os formatos
                result = get_daily_forecast(params.get('latitude'), params.get('longitude'),
                                            params.get('days_ahead', 3), self.cfg.open_meteo_url)

                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": "get_daily_forecast",
                    "content": result
                })

            # Segunda parte: gerar resposta final
            final_response = self.client.chat.completions.create(
                model=self.cfg.model,
                messages=self.messages,
                temperature=self.cfg.temperature,
                max_tokens=self.cfg.max_tokens
            )
            ans = final_response.choices[0].message.content

        else:
            # Se o modelo não identificou a necessidade de usar a ferramenta,
            # peça para o usuário fornecer as coordenadas novamente
            ans = ("Poderia repetir as coordenadas (latitude, longitude) e dias necessários"
                   " para que eu possa fornecer a previsão do tempo?")

        # Se o histórico estiver ligado, mantenha a conversa fluida,
        # caso contrário, limpe o histórico após cada resposta
        if self.cfg.history:
            self.messages.append({"role": "assistant", "content": ans})
        else:
            self.messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                }
            ]
        return ans

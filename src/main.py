from __future__ import annotations
import argparse
from src.agent.cli import run_cli
from gradio_ui import run_gradio
from src.agent.logging_utils import setup_logging
from src.agent.ollama_agent import OllamaAgent
from src.agent.settings import default_config


def main() -> None:
    setup_logging()  # Configura o logging antes de qualquer outra coisa
    config = default_config()  # Cria a configuração padrão, lendo valores das variáveis de ambiente ou usando defaults
    # Configura o parser de argumentos para permitir customização via linha de comando
    parser = argparse.ArgumentParser(description="Agente LLM via Ollama.")
    parser.add_argument("--base-url", type=str,
                        default=config.base_url, help="URL base da API Ollama.")
    parser.add_argument("--model", type=str,
                        default=config.model, help="Modelo LLM a ser usado.")
    parser.add_argument("--api-key", type=str,
                        default=config.api_key, help="Chave de API para autenticação.")
    parser.add_argument("--temperature", type=float,
                        default=config.temperature, help="Temperatura para geração de texto.")
    parser.add_argument("--max-tokens", type=int,
                        default=config.max_tokens, help="Número máximo de tokens na resposta.")
    parser.add_argument("--history", type=bool,
                        default=config.history, help="Habilitar ou desabilitar histórico de conversas.")
    parser.add_argument("--gradio", type=bool,
                        default=config.gradio, help="Executar a interface Gradio em vez do CLI.")

    # Sobrescreve a configuração com os valores fornecidos via linha de comando, se houver
    args = parser.parse_args()
    # Cria uma instância do agente Ollama usando a configuração final
    agent = OllamaAgent(config)

    # Decide se executa a interface Gradio ou o CLI
    if args.gradio:
        run_gradio(agent)
    else:
        run_cli(agent)


if __name__ == "__main__":
    main()

# MeteoAI
MeteoAI é um Agente LLM com Tool de Previsão do Tempo usando a API da Open-Meteo

## Requisitos
- Python 3.12+
- Ollama 0.8.0+
- Docker (opcional, para execução em contêiner)

## Estrutura do Projeto
```
MeteoAI/
├── .venv/
├── src/
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── logging_utils.py
│   │   ├── ollama_agent.py
│   │   ├── settings.py
│   │   └── weather_tool.py
│   ├── __init__.py
│   ├── gradio_ui.py
│   └── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Dependências
- `openai`: Para integração com a API da OpenAI.
- `gradio`: Para criar a interface de usuário.
- `python-dotenv`: Para carregar variáveis de ambiente do arquivo `.env`.
- `requests`: Para fazer chamadas HTTP à API de previsão do tempo.

## Como rodar o projeto
### Localmente
1. Clone o repositório:
   ```bash
   git clone
    cd MeteoAI
    ```
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente no arquivo `.env

5. Inicie o agente:
   ```bash
   python src/main.py
   ```
### Usando Docker
1. Certifique-se de ter o Docker instalado e em execução.
2. Construa a imagem Docker:
   ```bash
   docker compose build
   ```
3. Inicie o contêiner:
   ```bash
   docker compose up
   ```
4. Acesse a interface do agente em `http://localhost:7860`.

## Validação
Para validar as respostas do agente, você pode acessar o endpoint da Open-Meteo diretamente.
- Exemplo para São Paulo, Latitude -23.55, Longitude -46.63, pelos próximos 3 dias:
```
https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America/Sao_Paulo&forecast_days=3
```  

## Exemplos de Entrada e Saída
### Entrada
```
Pode me entregar a previsão para latitude -22.9068 e longitude -43.1729 para 3 dias? 
```
### Saída
```
Claro, aqui estão as previsões para cada dia:

* 10-03-2026
 + Temperatura máxima: 26,5°C
 + Temperatura mínima: 24,6°C
 + Precipitação de chuva: 1,2 mm

* 11-03-2026
 + Temperatura máxima: 24,6°C
 + Temperatura mínima: 22,3°C
 + Precipitação de chuva: 13 mm

* 12-03-2026
 + Temperatura máxima: 24,0°C
 + Temperatura mínima: 22,1°C
 + Precipitação de chuva: 20,9 mm
```

### Entrada
```
Qual a previsão para latitude -45.78, longitude -68.97, para daqui a 2 dias?
```
### Saída
```
Para a latitude -45.78, longitude -68.97, a previsão para a daqui a 2 dias é:

- 10 de março: Temperatura máxima: 23,2°C, Temperatura mínima: 10,3°C, Precipitação de chuva: 0,0 mm
- 11 de março: Temperatura máxima: 21,9°C, Temperatura mínima: 11,9°C, Precipitação de chuva: 0,0 mm
```

## Autor
- [Lucas Povinske](https://www.linkedin.com/in/lucas-josé-povinske-976893153/)
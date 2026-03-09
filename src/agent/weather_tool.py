import requests
import json


def get_daily_forecast(lat: float, lon: float, days_ahead: int, open_meteo_url) -> str:
    url = open_meteo_url  # Endpoint da API de previsão do tempo
    # Parâmetros para a API, incluindo latitude, longitude, tipos de dados diários e fuso horário
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "America/Sao_Paulo",
        "forecast_days": days_ahead
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return json.dumps(response.json())
    except Exception as e:
        return json.dumps({"error": f"Erro ao acessar API: {str(e)}"})


# Definição da ferramenta para previsão do tempo, seguindo o formato esperado pelo OllamaAgent
WEATHER_TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "get_daily_forecast",
        "description": "Obtém previsão do tempo para latitude e longitude específicas.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"},
                "days_ahead": {"type": "integer"}
            },
            "required": ["lat", "lon", "days_ahead"]
        }
    }
}

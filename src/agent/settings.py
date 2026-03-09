from dataclasses import dataclass

import os


@dataclass
class LLMConfig:
    base_url: str
    open_meteo_url: str
    model: str
    api_key: str
    temperature: float
    max_tokens: int
    history: bool
    gradio: bool


def default_base_url() -> str:
    return os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")  # URL padrão para a API Ollama


def open_meteo_url() -> str:
    return os.getenv("OPEN_METEO_URL", "https://api.open-meteo.com/v1/forecast")  # URL padrão para a API Open-Meteo


def default_model() -> str:
    return os.getenv("OLLAMA_MODEL", "llama3.2:1b")  # Modelo padrão


def default_api_key() -> str:
    return os.getenv("OLLAMA_API_KEY", "ollama")  # Chave de API padrão


def default_temperature() -> float:
    return float(os.getenv("OLLAMA_TEMPERATURE", "0.2"))  # Temperatura padrão


def default_max_tokens() -> int:
    return int(os.getenv("OLLAMA_MAX_TOKENS", "500"))  # Número máximo de tokens na resposta


# Habilita histórico por padrão, mas pode ser desabilitado via variável de ambiente
def history_enabled() -> bool:
    return os.getenv("HISTORY_ENABLED", "false").lower() in ("true", "1", "yes")


# Variável de ambiente para habilitar a interface Gradio
def gradio_enabled() -> bool:
    return os.getenv("GRADIO_ENABLED", "false").lower() in ("true", "1", "yes")


# Função para criar uma configuração padrão, lendo valores das variáveis de ambiente ou usando defaults
def default_config() -> LLMConfig:
    return LLMConfig(
        base_url=default_base_url(),
        open_meteo_url=open_meteo_url(),
        model=default_model(),
        api_key=default_api_key(),
        temperature=default_temperature(),
        max_tokens=default_max_tokens(),
        history=history_enabled(),
        gradio=gradio_enabled()
    )

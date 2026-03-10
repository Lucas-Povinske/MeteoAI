from __future__ import annotations
from src.agent.cli import run_cli
from gradio_ui import run_gradio
from src.agent.logging_utils import setup_logging
from src.agent.ollama_agent import OllamaAgent
from src.agent.settings import default_config


def main() -> None:
    setup_logging()
    config = default_config()
    agent = OllamaAgent(config)

    if config.gradio:
        run_gradio(agent)
    else:
        run_cli(agent)


if __name__ == "__main__":
    main()
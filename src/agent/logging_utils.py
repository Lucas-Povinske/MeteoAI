from __future__ import annotations

import logging
import os


# Configura o logging com base na variável de ambiente LOGLEVEL, ou INFO por padrão
def setup_logging() -> None:
    level = os.getenv("LOGLEVEL", "INFO").upper().strip()
    logging.basicConfig(
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

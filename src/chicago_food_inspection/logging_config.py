"""
Logging configuration.
"""

from __future__ import annotations

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

_CONFIGURED = False


def setup_logging(
    level: int = logging.INFO,
    log_file: Path | None = None,
    force: bool = False,
) -> None:
    """
    Configure the root logger with console and file handlers.

    Args:
        level: log level (int or str), defaults to logging.INFO
        log_file: path to the log file, if None default path is used
        force: forces logging configuration even if it has been configured
            Defaults to False.
    """

    global _CONFIGURED
    if _CONFIGURED and not force:
        return

    root_dir = Path(__file__).resolve().parent.parent.parent
    if log_file is None:
        log_dir = root_dir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "chicago_food_inspection.log"
    else:
        log_file.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    # Root at DEBUG so the file handler can capture full detail; third-party
    # DEBUG records are included by design. Revisit if noise becomes a problem.
    root_logger.setLevel(logging.DEBUG)
    for handler in root_logger.handlers[:]:
        handler.close()
        root_logger.removeHandler(handler)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """
    Retrieve a logger by name.

    Args:
        name: Logger name — typically pass __name__ from the calling module.

    Returns:
        A logging.Logger instance.
    """

    return logging.getLogger(name)


__all__ = ["setup_logging", "get_logger"]

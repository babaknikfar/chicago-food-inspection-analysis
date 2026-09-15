"""
Logging Configuration

"""

from pathlib import Path
import logging
import sys
from typing import Optional

_LOGGING_CONFIGURED = False

def configure_logging(
        log_file: Path = Path("logs/food_inspection.log"),
        log_level: str = "INFO",
        log_format: str = "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
) -> None:
    """
    Configure the root logger with console and file handlers.

    Args:
        log_file: Absolute path to the log file. Default to "logs/food_inspection.log"
        log_level: Log level name. Defaults to "INFO".
        log_format: Format string for log records.
    """

    global _LOGGING_CONFIGURED

    if _LOGGING_CONFIGURED:
        return

    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_level_number: int = getattr(logging, log_level.upper(), logging.INFO)
    formatter = logging.Formatter(log_format)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level_number)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(log_level_number)
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level_number)
    root_logger.handlers.clear()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    _LOGGING_CONFIGURED = True


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Retrieve a logger by name.

    Args:
        name: Logger name — typically pass __name__ from the calling module. If None, returns the root logger.
    
    Returns:
        A logging.Logger instance.
    """

    return logging.getLogger(name)
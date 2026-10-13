"""
Testing module for logging_config.py
"""

import logging
from collections.abc import Generator
from pathlib import Path

import pytest

import chicago_food_inspection.logging_config as logging_config
from chicago_food_inspection.logging_config import get_logger, setup_logging


@pytest.fixture(autouse=True)
def reset_logging_state() -> Generator[None, None, None]:
    """Reset logging state before and after every test for isolation."""

    def _cleanup():
        logging_config._CONFIGURED = False
        root = logging.getLogger()
        for handler in root.handlers[:]:
            handler.close()
            root.removeHandler(handler)

    _cleanup()
    yield
    _cleanup()


def test_logging_handlers(tmp_path: Path) -> None:
    log_file = tmp_path / "test.log"
    setup_logging(log_file=log_file, force=True)
    handlers = logging.getLogger().handlers
    assert len(handlers) == 2
    assert handlers[0].__class__.__name__ == "StreamHandler"
    assert handlers[1].__class__.__name__ == "RotatingFileHandler"


def test_idempotency(tmp_path: Path) -> None:
    log_file = tmp_path / "test.log"
    setup_logging(log_file=log_file, force=True)
    handlers_1 = list(logging.getLogger().handlers)
    setup_logging(log_file=tmp_path / "other.log")
    handlers_2 = list(logging.getLogger().handlers)
    assert handlers_1 == handlers_2


def test_reconfiguration(tmp_path: Path) -> None:
    log_file = tmp_path / "test.log"
    setup_logging(log_file=log_file, force=True)
    handlers_1 = list(logging.getLogger().handlers)
    setup_logging(log_file=log_file, force=True)
    handlers_2 = list(logging.getLogger().handlers)
    assert handlers_1 != handlers_2


def test_file_output(tmp_path: Path) -> None:
    log_file = tmp_path / "test.log"
    setup_logging(log_file=log_file, force=True)
    logging.getLogger().info("test info")
    for handler in logging.getLogger().handlers:
        handler.flush()
    with open(log_file, encoding="utf-8") as f:
        assert "test info" in f.read()


def test_file_handler_captures_below_console_level(tmp_path: Path) -> None:
    log_file = tmp_path / "test.log"
    setup_logging(level=logging.WARNING, log_file=log_file, force=True)
    logging.getLogger().info("test info")
    for handler in logging.getLogger().handlers:
        handler.flush()
    with open(log_file, encoding="utf-8") as f:
        assert "test info" in f.read()


def test_console_filters_below_level(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    log_file = tmp_path / "test.log"
    setup_logging(level=logging.WARNING, log_file=log_file, force=True)
    root = logging.getLogger()
    root.info("info message")
    root.warning("warning message")
    captured = capsys.readouterr()
    assert "info message" not in captured.out
    assert "warning message" in captured.out


def test_get_logger_returns_named_logger() -> None:
    logger = get_logger("test_name")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_name"

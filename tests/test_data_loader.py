"""
Testing module for data_loader.py
"""

from pathlib import Path

import pytest

from chicago_food_inspection.data_loader import load_data

FIXTURES_DIR = Path(__file__).parent / "fixtures"
TEST_CSV = FIXTURES_DIR / "test.csv"


def test_default_load() -> None:
    df = load_data(path=TEST_CSV)
    row, col = df.shape
    assert row == 10
    assert col == 4


def test_usecols() -> None:
    df = load_data(path=TEST_CSV, usecols=["integer", "float"])
    row, col = df.shape
    assert row == 10
    assert col == 2


def test_dtypes() -> None:
    df = load_data(
        path=TEST_CSV,
        dtypes={"integer": "int64", "float": "float64", "text": "string", "datetime": "string"},
    )
    assert str(df["text"].dtype) == "string"
    assert str(df["integer"].dtype) == "int64"
    assert str(df["datetime"].dtype) == "string"
    assert str(df["float"].dtype) == "float64"


def test_missing_file() -> None:
    with pytest.raises(FileNotFoundError):
        load_data(path=Path("does-not-exist"))


def test_missing_file_message() -> None:
    with pytest.raises(FileNotFoundError, match="Data file not found"):
        load_data(path=Path("does-not-exist.csv"))


def test_logging_on_load(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level("INFO"):
        load_data(path=TEST_CSV)
    assert "Loaded 10 rows" in caplog.text

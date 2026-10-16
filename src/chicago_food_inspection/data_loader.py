"""
Data loader module.
"""

from pathlib import Path

import pandas as pd

from chicago_food_inspection.logging_config import get_logger
from chicago_food_inspection.paths import PROJECT_ROOT, RAW_DATA_FILE

logger = get_logger(__name__)


def load_data(
    path: Path = RAW_DATA_FILE,
    *,
    usecols: list[str] | None = None,
    dtypes: dict[str, str] | None = None,
    low_memory = False,
) -> pd.DataFrame:
    """Load a CSV dataset from disk.

    Args:
        path: Path to the CSV file. Defaults to the raw data file.
        usecols: Subset of columns to load. If None, all columns are loaded.
        dtypes: Mapping of column name to pandas dtype string. If None,
            pandas infers types.

    Returns:
        A pandas DataFrame.

    Raises:
        FileNotFoundError: If ``path`` does not point to an existing file.
    """

    if not path.is_file():
        raise FileNotFoundError(
            f"Data file not found: {path}\n"
            f"Download the dataset from the Chicago Data Portal and place it at: {path}"
        )

    df = pd.read_csv(path, encoding="utf-8", usecols=usecols, dtype=dtypes, low_memory=low_memory)
    rows, cols = df.shape
    memory_mb = df.memory_usage(deep=True).sum() / (1024**2)

    logger.info(
        "Loaded %d rows × %d columns from %s (%.1f MB in memory)",
        rows,
        cols,
        path.relative_to(PROJECT_ROOT),
        memory_mb,
    )

    return df

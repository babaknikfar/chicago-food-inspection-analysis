"""
Testing module for paths.py
"""

from chicago_food_inspection import paths


def test_project_root_contains_pyproject() -> None:
    assert (paths.PROJECT_ROOT / "pyproject.toml").is_file()


def test_data_dirs_are_under_project_root() -> None:
    assert paths.DATA_DIR.parent == paths.PROJECT_ROOT
    assert paths.RAW_DATA_DIR.parent == paths.DATA_DIR
    assert paths.PROCESSED_DATA_DIR.parent == paths.DATA_DIR


def test_reports_and_figures_are_nested() -> None:
    assert paths.REPORTS_DIR.parent == paths.PROJECT_ROOT
    assert paths.FIGURES_DIR.parent == paths.REPORTS_DIR


def test_logs_dir_under_project_root() -> None:
    assert paths.LOGS_DIR.parent == paths.PROJECT_ROOT

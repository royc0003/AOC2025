from pathlib import Path

# ===========================
# Path Constants
# ===========================
REPO_ROOT = Path(__file__).resolve().parents[1]
CONSTANT_PATH = REPO_ROOT / "constants" / "constants.py"
UTILS_PATH = REPO_ROOT / "utils" / "_file_utils.py"
DAY_1_INPUT_PATH = REPO_ROOT / "day1" / "input" / "input.txt"
DAY_1_TEST_CASE_1 = REPO_ROOT / "day1" / "input" / "testcase1.txt"
__all__ = [
    "REPO_ROOT",
    "CONSTANT_PATH",
    "UTILS_PATH",
    DAY_1_INPUT_PATH
]

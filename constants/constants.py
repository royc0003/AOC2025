from pathlib import Path

# ===========================
# Path Constants
# ===========================
REPO_ROOT = Path(__file__).resolve().parents[1]
CONSTANT_PATH = REPO_ROOT / "constants" / "constants.py"
UTILS_PATH = REPO_ROOT / "utils" / "_file_utils.py"
DAY_1 = "day1"
INPUT = "input"
DAY_2 = "day2"
DAY_1_INPUT_PATH = REPO_ROOT / DAY_1 / INPUT / "input.txt"
DAY_1_TEST_CASE_1 = REPO_ROOT / DAY_1 / INPUT / "testcase1.txt"
DAY_2_INPUT_PATH = REPO_ROOT / DAY_2 / INPUT / "input.txt"
DAY_2_TEST_CASE_1 = REPO_ROOT / DAY_2 / INPUT / "testcase2.txt"
__all__ = [
    "REPO_ROOT",
    "CONSTANT_PATH",
    "UTILS_PATH",
    DAY_1_INPUT_PATH,
    DAY_1_TEST_CASE_1,
    DAY_2_INPUT_PATH,
    DAY_2_TEST_CASE_1,
]

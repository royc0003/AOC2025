from pathlib import Path

# ===========================
# Path Constants
# ===========================
REPO_ROOT = Path(__file__).resolve().parents[1]
CONSTANT_PATH = REPO_ROOT / "constants" / "constants.py"
UTILS_PATH = REPO_ROOT / "utils" / "_file_utils.py"

__all__ = [
    "REPO_ROOT",
    "CONSTANT_PATH",
    "UTILS_PATH",
]

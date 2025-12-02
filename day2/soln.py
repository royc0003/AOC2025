from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# Necessary imports
from constants import CONSTANT_PATH, UTILS_PATH, DAY_1_INPUT_PATH, DAY_1_TEST_CASE_1
from utils import load_file_from_input_path
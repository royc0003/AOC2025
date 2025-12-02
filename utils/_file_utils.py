# Universal Functions
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# load file
def load_file_from_input_path(input_file_path: Path) -> list:
    """
    Returns a list of input from the input_file_path
    """
    res = []
    try:
        with open(input_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                res.append(line)
            return res
    except:
        raise Exception("Input file is not handled correctly")

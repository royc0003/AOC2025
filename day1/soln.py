# Set up repository root so sibling packages resolve when running this file directly
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# Necessary imports
from constants import CONSTANT_PATH, UTILS_PATH, DAY_1_INPUT_PATH
from utils import load_file_from_input_path


def split_command(command: str) -> list[str, str]:
    '''
    splits the command into
    (1) direction and (2) amount
    e.g. L50
    [L, 50]
    '''
    res: list = []
    return res[str(command[0]), str(command[1:])]

# Universal Import Functions
day_1_inputs: list[str] = load_file_from_input_path(DAY_1_INPUT_PATH)

# ranges from 0 - 99
total_zeroes: int = 0
res = 0
for command in day_1_inputs:
    _direction, _amount = split_command(command)
    opt  = 1
    lower_direction = _direction.lower()
    match lower_direction:
        case 'l':
            if opt >= 0:
                opt *= -1
        case 'r':
            if opt < 0:
                opt *= -1
        case _:
            print("unknown direction")
            raise(Exception("Unknown direction provided"))

    _amount *= opt  # sets the sign
    _amount %= 100
    res += _amount
    if res == 0:
        total_zeroes += 1
print(total_zeroes)

    


    
    






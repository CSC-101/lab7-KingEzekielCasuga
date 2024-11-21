from typing import Optional

# Task 1
# str_to_float

# ensures a proper conversion from string input to float, and if there is
# a value error then it will return none

def str_to_float(string:str) -> Optional[float]:
    try:
        return float(string)
    except ValueError:
        return None

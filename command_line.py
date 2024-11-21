import sys

from convert import str_to_float

# task 3
#reads the command line for the file and adds the total of such, and returns it

def process_command_line_args() -> float:
    total = 0.0
    for arg in sys.argv:
        if str_to_float(arg) != None:
            total += str_to_float(arg)
    return total

if __name__ == '__main__':
    print(process_command_line_args())
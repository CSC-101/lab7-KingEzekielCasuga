# Task 2
# gather numbers
from convert import str_to_float

# takes in no parameters but creates a new list that is made up of inputs
# of floats from the user, ensures that they are all floats

def gather_numbers() -> list[float]:
    numbers = []
    while True:
        user_input = input('Enter a number')
        if user_input == 'done':
            break
        else:
            if str_to_float(user_input) != None:
                numbers.append(str_to_float(user_input))
    return numbers



if __name__ == "__main__":
    gather_numbers()



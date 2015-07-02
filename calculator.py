"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculate_stuff():
    """ This function prompts the user to perform basic math using prefix notation.

    Takes no arguments and returns nothing.
    """
    input_string = 'start'
    while 'q' not in input_string:
        # Runs program until the user types in 'q'.

        input_string = raw_input("> ")
        print input_string

        input_list = input_string.split(" ")        

        i = 1
        while i < len(input_list):
            input_list[i] = int(input_list[i])
            i += 1
        list_checker(input_list)
        
def list_checker(input_list):

    if input_list[0] == type(str) and input_list[1:] == type(int):
        return math_function_picker(input_list)
    else:
        # import pdb; pdb.set_trace()
        print input_list #figure out what the types of the elements of htis list are.
        return


def math_function_picker(input_list):

        # Converts user input into integers.


        if input_list[0] == "+" and len(input_list) == 3:
            print add(input_list[1], input_list[2])
        elif input_list[0] == "-" and len(input_list) == 3:
            print subtract(input_list[1], input_list[2])
        elif input_list[0] == "*" and len(input_list) == 3:
            print multiply(input_list[1], input_list[2])
        elif input_list[0] == "/" and len(input_list) == 3:
            print divide(input_list[1], input_list[2])
        elif input_list[0] == "square" and len(input_list) == 2:
            print square(input_list[1])
        elif input_list[0] == "cube" and len(input_list) == 2:
            print cube(input_list[1])
        elif input_list[0] == "pow" and len(input_list) == 3:
            print power(input_list[1], input_list[2])
        elif input_list[0] == "mod" and len(input_list) == 3:
            print mod(input_list[1], input_list[2])
        else:
            print "I don't understand"

calculate_stuff()
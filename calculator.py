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
    exit_token = None
    while exit_token != 'q':
        input_string = raw_input("> ")
        input_list = input_string.split(" ")
        
        i = 1
        while i < len(input_list):
            input_list[i] = int(input_list[i])
            i += 1

        if input_list[0] == "+":
            print add(input_list[1], input_list[2])
        elif input_list[0] == "-":
            print subtract(input_list[1], input_list[2])
        elif input_list[0] == "*":
            print multiply(input_list[1], input_list[2])
        elif input_list[0] == "/":
            print divide(input_list[1], input_list[2])
        elif input_list[0] == "square":
            print square(input_list[1])
        elif input_list[0] == "cube":
            print cube(input_list[1])
        elif input_list[0] == "pow":
            print power(input_list[1], input_list[2])
        elif input_list[0] == "mod":
            print mod(input_list[1], input_list[2])
        elif 'q' in input_string:
            break
        else:
            print "I don't understand"

calculate_stuff()
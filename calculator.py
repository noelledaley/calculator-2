"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculate_stuff():
    exit_token = None
    while exit_token != 'q':
        input_string = raw_input("> ")
        input_list = input_string.split(" ")
        if input_list[0] == "+":
            add(input_list[1], input_list[2])
        elif (subtract):
                do the subtracty thing
        elif (multiply):

        elif (divide):

        elif (square):

        elif (cube):

        elif (power):

        elif (mod):

        elif q in input_string:
            break
        else:
            print "I don't understand"
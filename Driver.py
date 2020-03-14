import MathOperators

# FileName: Driver.py
# Author: Anthony Pompili
# Date: March 13, 2020
# Description: This file holds the main logic for the Calculator application. This file will launch
# the calculator GUI, and allow the user to perform the specified operations allowed in the interface.

# Starting point of calculator application:
user_input = input("What operation would you like to perform?")

# Simple check to see what operation they selected
if user_input == "Add":
    number1 = input("Number1: ")
    number2 = input("Number2: ")
    print(MathOperators.addition(number1, number2))
elif user_input == "Sub":
    number1 = input("Number1: ")
    number2 = input("Number2: ")
    print(MathOperators.subtraction(number1, number2))
elif user_input == "Divide":
    number1 = input("Number1: ")
    number2 = input("Number2: ")
    print(MathOperators.divide(number1, number2))
elif user_input == "Multiply":
    number1 = input("Number1: ")
    number2 = input("Number2: ")
    print(MathOperators.multiply(number1, number2))
else:
    print("Invalid input.")
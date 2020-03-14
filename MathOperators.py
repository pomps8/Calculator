# FileName: MathOperators.py
# Author: Anthony Pompili
# Date: March 13, 2020
# Description: This file holds all of the arithemtic / numerical operators for our calculator.
# This includes checking if input is a valid number, a valid float or valid int, and the actual
# operators of addition, subtraction, multiplication and division.

# Function Name: multiply
# Parameters: number1 (integer / float), number2 (integer / float)
# Return type: if result is valid, returns number1 x number2, else returns "Bad input"
# Description: Takes two numbers and performs the multiplication of the two numbers.
def multiply(number1, number2):
    # If both numbers are valid numbers
    # After computation, check if the float is an int (ex: 19.0 is an int, so we can cast this).
    # Else, just return the result as a float.
    if check_valid_number(number1) and check_valid_number(number2):
        result = float(number1) * float(number2)
        if result.is_integer():
            return int(result)
        else:
            return result
    return "Bad Input"
    # If the number fails the check_valid_number, an exception is thrown

# Function Name: divide
# Parameters: number1 (integer / float), number2 (integer / float)
# Return type: if result is valid, returns number1 / number2, else returns "Bad input"
# Description: Takes two numbers and performs the division of the two numbers.
def divide(number1, number2):
    # If both numbers are valid numbers.
    # After computation, check if the float is an int (ex: 19.0 is an int, so we can cast this).
    # Else, just return the result as a float.
    if check_valid_number(number1) and check_valid_number(number2):
        result = float(number1) / float(number2)
        if result.is_integer():
            return int(result)
        else:
            return result
    return "Bad Input"

# Function Name: add
# Parameters: number1 (integer / float), number2 (integer / float)
# Return type: if result is valid, returns number1 + number2, else returns "Bad input"
# Description: Takes two numbers and performs the addition of the two numbers.
def addition(number1, number2):
    # If both numbers are valid numbers.
    # After computation, check if the float is an int (ex: 19.0 is an int, so we can cast this).
    # Else, just return the result as a float.
    if check_valid_number(number1) and check_valid_number(number2):
        result = float(number1) + float(number2)
        if result.is_integer():
            return int(result)
        else:
            return result
    return "Bad Input"

# Function Name: subtraction
# Parameters: number1 (integer / float), number2 (integer / float)
# Return type: if result is valid, returns number1 x number2, else returns "Bad input"
# Description: Takes two numbers and performs the multiplication of the two numbers.
def subtraction(number1, number2):
    # If both numbers are valid numbers.
    # After computation, check if the float is an int (ex: 19.0 is an int, so we can cast this).
    # Else, just return the result as a float.
    if check_valid_number(number1) and check_valid_number(number2):
        result = float(number1) - float(number2)
        if result.is_integer():
            return int(result)
        else:
            return result
    return "Bad Input"

# Function Name: check_valid_number
# Parameters: number (integer / float)
# Return type: True if the input is a valid number, otherwise false
# Description: This function attempts to convert the input (number) to a float, if
# it is successful, then it is a valid number (floats can be converted to floats, and
# ints can be converted to floats, any other type of input cannot.
def check_valid_number(number):
    try:
        float(number)  # Type-casting the string to `float`.
        # If string is not a valid `float`,
        # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

# Function Name: is_valid_int
# Parameters: number (integer / float)
# Return type: True if the input is a valid int, otherwise false
# Description: This function checks to see if the input (number) is a int.
def is_valid_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

# Function Name: is_valid_float
# Parameters: number (integer / float)
# Return type: True if the input is a valid float, otherwise false
# Description: This function checks to see if the input (number) is a float.
def is_valid_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

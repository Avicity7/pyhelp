# Multiplication.py

"""
In Python, the * sign is used to refer to multiplication.
However, multiplication is not entirely constrained to integers and floats only.
"""

# Multiplication with strings and integers
myString = "HelloWorld"
print(myString * 3)                 # Prints out HelloWorldHelloWorldHelloWorld

# Multiplication with integers
integerA = 2
integerB = 1
integerResult = integerA * integerB  
print(integerResult)                 # Prints out 2

# Multiplication with floats
floatA = 1.5
floatB = 2.5
floatResult = floatA * floatB
print(floatResult)                   # Prints out 3.75

# Multiplication with floats and integers
"""
Note:
As of Python 3+, integers will be automatically converted to floats to give you the expected value.
"""
numberResult = integerA * floatB
print(numberResult)                  # Prints out 5.0

# You cannot multiply lists.

# You cannot multiply dictionaries.


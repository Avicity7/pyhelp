# Multiplication.py

"""
In Python, the * sign is used to refer to multiplication.
However, subtraction is not entirely constrained to integers and floats only.
"""

# Multiplication with strings
myString = "HelloWorld"
print(myString * 3)                 # Prints out HelloWorldHelloWorldHelloWorld

# Multiplication with integers
integerA = 2
integerB = 1
integerTotal = integerA * integerB  
print(integerTotal)                 # Prints out 2

# Subtraction with floats
floatA = 1.5
floatB = 2.5
floatTotal = floatA * floatB
print(floatTotal)                   # Prints out 3.75

# Subtraction with floats and integers
"""
Note:
As of Python 3+, integers will be automatically converted to floats to give you the expected value.
"""
numberTotal = integerA * floatB
print(numberTotal)                  # Prints out 5.0

# You cannot multiply lists.

# You cannot multiply dictionaries.


# Subtraction.py

"""
In Python, the - sign is used to refer to subtraction.
However, unlike addition, subtraction is mostly entirely constrained to integers and floats only.
"""

# Subtraction with integers
integerA = 2
integerB = 1
integerResult = integerA - integerB  
print(integerResult)                 # Prints out 1

# Subtraction with floats
floatA = 1.5
floatB = 2.5
floatResult = floatA - floatB
print(floatResult)                   # Prints out -1.0

# Subtraction with floats and integers
"""
Note:
As of Python 3+, integers will be automatically converted to floats to give you the expected value.
"""
numberResult = integerA - floatB
print(numberResult)                  # Prints out 0.5

# You cannot subtract lists.

# You cannot subtract dictionaries.


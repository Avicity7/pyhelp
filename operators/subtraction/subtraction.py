# Subtraction.py

"""
In Python, the - sign is used to refer to subtraction.
However, subtraction is not entirely constrained to integers and floats only.
In fact, you're able to subtract almost all common types of Python together!
"""

# Subtraction with integers
integerA = 2
integerB = 1
integerTotal = integerA - integerB  
print(integerTotal)                 # Prints out 1

# Subtraction with floats
floatA = 1.5
floatB = 2.5
floatTotal = floatA - floatB
print(floatTotal)                   # Prints out -1.0

# Subtraction with floats and integers
"""
Note:
As of Python 3+, integers will be automatically converted to floats to give you the expected value.
"""
numberTotal = integerA - floatB
print(numberTotal)                  # Prints out 0.5

# You cannot subtract lists.

# You cannot add dictionaries together.


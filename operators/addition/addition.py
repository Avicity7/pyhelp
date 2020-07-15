# Addition.py

"""
In Python, the + sign is used to refer to addition.
However, addition is not entirely constrained to integers and floats only.
In fact, you're able to add almost all common types of Python together!
"""

# Addition with integers
integerA = 1
integerB = 2
integerTotal = integerA + integerB  
print(integerTotal)                 # Prints out 3

# Addition with floats
floatA = 1.5
floatB = 2.5
floatTotal = floatA + floatB
print(floatTotal)                   # Prints out 4.0

# Addition with floats and integers
"""
Note:
As of Python 3+, integers will be automatically converted to floats to give you the expected value.
"""
numberTotal = integerA + floatB
print(numberTotal)                  # Prints out 4.5

# Addition with lists
listA = ['hello', 'world']
listB = ['welcome', 'to', 'GitHub']
listTotal = listA + listB
print(listTotal)                    # Prints out ['hello', 'world', 'welcome', 'to', 'GitHub']

# You cannot add dictionaries together.

"""
Python also supports adding values to variables.
Note that the type of what you're trying to add must match the type of the original variable.
Only integers and floats are excluded from this rule.
"""
myString = 'Hello '
myString += 'world'
print(myString)                     # Prints out Hello world

myInt = 50
myInt += 10
print(myInt)                        # Prints out 60

myFloat = 5.5
myFloat += 4.0
print(myFloat)                      # Prints out 9.5

myInt += myFloat
print(myInt)                        # Prints out 69.5
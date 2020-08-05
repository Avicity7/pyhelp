# Division.py

"""
In Python, the / sign is used to refer to division.
However, division is mostly entirely constrained to integers and floats only.
"""

# Division with integers
integerA = 5
integerB = 2
integerResult = integerA / integerB
print(integerResult)                 # Prints out 2.5

# Division with floats
floatA = 5.62
floatB = 2.22
floatResult = floatA / floatB
print(floatResult)                   # Prints out 2.5315315315315314

# Division with integers and floats
numberResult = integerA / floatB
print(numberResult)                  # Prints out 2.252252252252252

# Floor division
"""
In Python, normal division always returns a float.
If you'd like to take the integer (and disregarding the decimal value), use floor division.
The // sign is used to refer to floor division.
"""
numberResult = integerA // floatB
print(numberResult)                  # Prints out 2
# Gets the user to input a temperature.
temp = input('Enter a temperature (in °C!): ')

# Tries to type cast the user's input into an integer.
# If it fails, it's likely because the user has entered an alphabet or symbol (ValueError).
try:
    temp = int(temp)
except ValueError:
    print('The input is invalid!')

# The variable that stores the temperature's description.
description = ''

# Checks if the temperature is -30 or below and applies the appropriate description.
if (temp <= -30):
    description = 'Really cold!'
# Otherwise, check if the temperature is between -29 and 0 and applies the appropriate description.
elif (temp >= -29 and temp <= 0):
    description = 'Pretty cold'
# Otherwise, check if the temperature is between 1 and 15 and applies the appropriate description.
elif (temp >= 1 and temp <= 15):
    description = 'Pretty average'
# Otherwise, check if the temperature is between 16 and 25 and applies the appropriate description.
elif (temp >= 16 and temp <= 25):
    description = 'Pretty warm'
# Otherwise, check if the temperature is between 26 and 32 and applies the appropriate description.
elif (temp >= 26 and temp <= 32):
    description = 'Fairly hot'
# Otherwise, when all else fails, the temperature is above 32. The appropriate description is used.
else:
    description = 'Really hot!'

# Outputs/Prints out the value of description.
print(description)
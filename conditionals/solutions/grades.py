# Gets the user to input a score.
score = input('Enter a score: ')

# Tries to type cast the user's input into an integer.
# If it fails, it's likely because the user has entered an alphabet or symbol (ValueError).
try:
    score = int(score)
except ValueError:
    print('The input is invalid!')

# The variable that stores the score's grade.
grade = ''

# Checks if the score is 75 and above. If so, the score has a grade of A1.
if (score >= 75):
    grade = 'A1'
# Otherwise, check if the score between 70 and 74 (inclusive). If so, the score has a grade of A2.
elif (score >= 70 and score <= 74):
    grade = 'A2'
# Otherwise, check if the score between 65 and 69 (inclusive). If so, the score has a grade of B3.
elif (score >= 65 and score <= 69):
    grade = 'B3'
# Otherwise, check if the score between 60 and 64 (inclusive). If so, the score has a grade of B4.
elif (score >= 60 and score <= 64):
    grade = 'B4'
# Otherwise, check if the score between 55 and 59 (inclusive). If so, the score has a grade of C5.
elif (score >= 55 and score <= 59):
    grade = 'C5'
# Otherwise, check if the score between 50 and 54 (inclusive). If so, the score has a grade of C6.
elif (score >= 50 and score <= 54):
    grade = 'C6'
# Otherwise, check if the score between 45 and 49 (inclusive). If so, the score has a grade of D7.
elif (score >= 45 and score <= 49):
    grade = 'D7'
# Otherwise, check if the score between 40 and 44 (inclusive). If so, the score has a grade of E8.
elif (score >= 40 and score <= 44):
    grade = 'E8'
# Otherwise, when all else fails, the score is below 40. The score has a grade of F9.
else:
    grade = 'F9'

# Outputs/Prints out the value of grade.
print(grade)
    
from typing import Type
Grades = float(input("What grade percentage did you attain this semester?: "))


if Grades >= 65 and Grades <= 75:
    print("5.0")
    print("Failure")
elif Grades == 75:
    print("3.0")
    print("Passing")
elif Grades >= 76 and Grades <= 79:
    print("2.75")
    print("Satisfactory")
elif Grades >= 79 and Grades <= 82:
    print("2.5")
    print("Satisfactory")
elif Grades >= 82 and Grades <= 85:
    print("2.25")
    print("Good")
elif Grades >= 85 and Grades <= 88:
    print("2.0")
    print("Good")
elif Grades >= 88 and Grades <= 91:
    print("1.75")
    print("Very Good")
elif Grades >= 91 and Grades <= 94:
    print("1.5")
    print("Very Good")
elif Grades >= 94 and Grades <= 97:
    print("1.25")
    print("Excellent")
elif Grades >= 97 and Grades <= 100:
    print("1.0")
    print("Excellent")
else:
    Inc = input("Have you completed all your requirements including major exam?: ")
    if Inc == ("Yes"):
        print("Congratulations, you passed.")
    elif Inc == ("No"):
        print("Unfortunately, you are incomplete.")
    else:
        Withdrawn = input("Did you withdraw from the university?: ")
        if Withdrawn == ("Yes"):
            print("Goodluck with your future endeavours.")
        else:
            Dropped = input("Do you have any record of not attending classes since the start of the year?: ")
            if Dropped == ("Yes"):
                print("Unfortunately, you have been dropped from the university. Goodluck!")
            elif Dropped == ("No"):
                print("You should have a conversation about this with your instructor.")        


import math
def GradesRoundOff(Grades, decimals=0):
    multiplier = 10**decimals
    return math.floor(Grades*multiplier + 0.5)/multiplier

GradesRoundOff(Grades)
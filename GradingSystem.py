from typing import Type
# First of all, my program will require you to input your grade for the semester.
Grades = float(input("What grade percentage did you attain this semester?: "))


# This is a function which performs the rounding-off of the float value you provided above.
import math
def GradesRoundOff(Grades, decimals=0):
    multiplier = 10**decimals
    return math.floor(Grades*multiplier + 0.5)/multiplier


# Then this variable will execute the function.
GradeMoRoundedOff = GradesRoundOff(Grades)


print(int(GradeMoRoundedOff))


# This if-elif-else statementes, will evaluate your provided grade, on where it is classfied  whether your failed or did good 
# during your semester. 
if GradeMoRoundedOff >= 65 and Grade <= 75:
    print("5.0")
    print("Failure")
elif Grades == 75:
    print("3.0")
    print("Passing")
elif Grades >= 76 and Grades <= 78:
    print("2.75")
    print("Satisfactory")
elif Grades >= 79 and Grades <= 81:
    print("2.5")
    print("Satisfactory")
elif Grades >= 82 and Grades <= 84:
    print("2.25")
    print("Good")
elif Grades >= 85 and Grades <= 87:
    print("2.0")
    print("Good")
elif Grades >= 88 and Grades <= 90:
    print("1.75")
    print("Very Good")
elif Grades >= 91 and Grades <= 93:
    print("1.5")
    print("Very Good")
elif Grades >= 94 and Grades <= 96:
    print("1.25")
    print("Excellent")
elif Grades >= 97 and Grades <= 100:
    print("1.0")
    print("Excellent")
    
# To add, the program will also evaluate you if you are incomplete. Another condition is if you withdrawn from the university, or you did 
# not attend any class that says you are dropped.          
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
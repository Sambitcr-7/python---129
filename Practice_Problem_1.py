# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:

#1. Do not use any type of modules like DateTime or date utils. (-5 points)
#2. Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
#3. Your code should handle all sort of errors like:                       (2 points)
# . You are not yet born
# . You seem to be the oldest person alive
# . You can also handle any other errors, if possible!



yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge  

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")


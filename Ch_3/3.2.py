# Get user input of the score and print an error if it's not within the correct range
try:
    score = float(input("Enter a score between 0.0 and 1.0:"))
except:
    print("You didn't enter a score within the given range.")
    exit()

if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
else:
    print("You didn't enter a score within the given range.")
    exit()

print(grade)
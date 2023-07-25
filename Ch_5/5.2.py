# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and 
# smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore 
# the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Desired output:
# Invalid input
# Maximum is 10
# Minimum is 2

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
    except:
        print("Invalid input")
        continue
    
    if largest == None:
        largest = num
    elif num > largest:
        largest = num
    
    if smallest == None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
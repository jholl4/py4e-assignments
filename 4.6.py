# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and
# time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and 
# use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program
# (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the 
# user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h, r):
    """This function will accept the hours and hourly pay rate as arguments and calculate the total gross pay from the values passed."""
    # Convert h to a float
    hrs = float(h)
    # Convert r to a float
    rt = float(r)
    otRt = 1.5 * rt
    if hrs <= 40:
        # Calculate the normal pay rate for 40 hours or less
        grossPay = hrs * rt
    else:
        # Calculate normal pay for the first 40 hours plus overtime pay for anything over 40
        otHrs = hrs - 40
        otPay = otHrs * otRt
        normPay = rt * 40
        grossPay = normPay + otPay
    return grossPay

usrHrs = input("Enter Hours:")
usrRt = input("Enter Rate:")
p = computepay(usrHrs, usrRt)
print("Pay", p)
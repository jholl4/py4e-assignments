hrs = input("Enter Hours:")
# Convert hours input to a float for use in calculations
h = float(hrs)
rate = input("Enter rate:")
# Convert rate input to a float for use in calculations
r = float(rate)
# The overtime pay rate
otRt = 1.5 * r

if h <= 40:
    # Calculate the normal pay rate for 40 hours or less
    grossPay = h * r
else:
    # Calculate normal pay for the first 40 hours plus overtime pay for anything over 40
    otHrs = h - 40
    otPay = otHrs * otRt
    normPay = r * 40
    grossPay = normPay + otPay

# Print the result of the pay calculation
print(grossPay)
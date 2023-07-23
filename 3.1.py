hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
# The overtime pay rate
otRt = 1.5 * r

if hrs <= 40:
    grossPay = h * r
else:
    otHrs = hrs - 40
    otPay = otHrs * otRt
    normPay = r * 40
    grossPay = normPay + otPay
    
print(grossPay)
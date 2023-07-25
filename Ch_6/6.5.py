# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

pos1 = text.find('0')
pos2 = text.find('5')
num = float(text[pos1:pos2+1])

print(num)
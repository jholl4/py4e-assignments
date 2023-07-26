# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that
# maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.

# Desired output: cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Dictionary to store all emails and counts of how many times they appear
emailDict = {}

# Read through each line in the file, skip lines that don't contain "From:" and add the second word (email) to the dictionary
for line in handle:
    if "From:" not in line:
        continue
    email = line.split()[1]
    emailDict[email] = emailDict.get(email, 0) + 1

# Variables to store the highest-occurring email address and its respective value
maxEmail = None
maxNum = None

# print(emailDict)

# Check through dictionary and see which email/key has the highest value
for key, val in emailDict.items():
    if maxNum == None or val > maxNum:
        maxEmail = key
        maxNum = val
        
# Print the highest-value email address and the number of times it appeared
print(maxEmail, maxNum)
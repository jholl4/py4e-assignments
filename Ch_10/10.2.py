# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Desired output:
    
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Create dictionary to store hours of the day as keys and counts of occurrences for each hour as values
dict = {}

# Read through the lines, ignoring lines that don't contain "From:", and extract the hour from the time "word"
for line in handle:
    if "From " not in line:
        continue
    time = line.split()[5]
    hr = time.split(":")[0]
    # Add key: hr val: count to dictionary
    dict[hr] = dict.get(hr, 0) + 1

# Printing for debugging
# print(dict)

# Create a list of sorted tuples generated from the dictionary
lst = sorted( dict.items() )

# Iterate through the list of tuples, printing each tuple individually
for k, v in lst:
    print(k, v)
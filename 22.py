# Euler Problem 22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?


# file can be found at https://projecteuler.net/problem=22
with open(r'C:\Users\benja\Downloads\p022_names.txt', 'r') as file:
    line = file.readline()
    names_str = ''
    count = 1
    while line:
        names_str += line
        line = file.readline()
        count += 1

# Remove leading and trailing "
names_str = names_str[1:len(names_str) - 1]
# Split into list, removing all ","
names_str = names_str.split('\",\"')

# Sort alphabetically
names_str.sort()

sum_of_scores = 0

for i in range(0,len(names_str)):
    alpha_val = 0
    name = names_str[i]
    for letter in name:
        alpha_val += ord(letter) - 64
    sum_of_scores += (alpha_val * (i+1))

print(sum_of_scores)
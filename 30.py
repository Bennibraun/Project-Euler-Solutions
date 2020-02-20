# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


sols = []
num = 2
sum = 0

while True:
    sum = 0
    num_list = [int(x) for x in str(num)]
    for digits in num_list:
        sum += digits**5
    if sum == num:
        print(num)
        sols.append(num)
    num += 1
    if num > 200000:
        break

total = 0
for n in sols:
    total += n

print(total)
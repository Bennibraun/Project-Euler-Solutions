# Euler Problem 28

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101. //Note: don't double-count the crossover

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import math


def diag_count(start,n):
    diag_sum = 0
    incr = start
    prev = 1
    for i in range(0, int(n/2)):
        diag_sum += prev+incr
        prev += incr
        incr += 8
    return diag_sum

n = 1001
total = 1
for i in range(2,9,2):
    total += diag_count(i,n)
print(total)

# 73 74 75 76 77 78 79 80 81
# 72 43 44 45 46 47 48 49 50
# 71 42 21 22 23 24 25 26 51
# 70 41 20  7  8  9 10 27 52
# 69 40 19  6  1  2 11 28 53
# 68 39 18  5  4  3 12 29 54
# 67 38 17 16 15 14 13 30 55
# 66 37 36 35 34 33 32 31 56
# 65 64 63 62 61 60 59 58 57

# diagonals exhibit constant secondary pattern:
# 1 7 21 43 73
#  6 14 22 30
#   8  8  8

# 1 3 13 31 57
#  2 10 18 26
#   8  8  8

# 1 9 25 49 81
#  8 16 24 32
#   8  8  8

# 1 5 17 37 65
#  4 12 20 28
#   8  8  8
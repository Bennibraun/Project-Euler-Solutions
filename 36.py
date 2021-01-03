# Euler Problem 36

# The decimal number, 585 = 1001001001b, is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

import math

def isPalindromic(n):
    n = str(n)
    for i in range(0, int(len(n) / 2)):
        if n[i] != n[len(n)-i-1]:
            return False
    return True

pal_sum = 0
for n in range(1, 1000000):
    if isPalindromic(n):
        bn = bin(n)[2:]
        if isPalindromic(int(bn)):
            pal_sum += n

print(pal_sum)
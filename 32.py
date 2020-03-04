# Euler Problem 32

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import math


# find all combinations of 1-9
# for each, find all multiplicand/multiplier/product combination

# 9! different combos of 1-9


products = []

# finds all possible permutations of the list
# s = the list
# a = starting index
# b = ending index
def permute(s, a, b):
    if a==b:
        isPandigitalProduct(s)
    else:
        for i in range(a,b+1):
            s[a], s[i] = s[i], s[a]
            permute(s, a+1, b)
            # For efficiency. There are no instances of pandigital products that don't start with 1.
            if s[0] >= 2:
                break
            s[a], s[i] = s[i], s[a] #backtrack


def isPandigitalProduct(p):
    global count
    # Loop through possible lengths of first value
    # 0-j, j-k, k-end
    for j in range(1,8):
        for k in range(j+1,9):
            a = [str(digit) for digit in p[:j]]
            a = int(''.join(a))
            b = [str(digit) for digit in p[j:k]]
            b = int(''.join(b))
            c = [str(digit) for digit in p[k:]]
            c = int(''.join(c))
            if a * b == c and c not in products:
                products.append(c)
                print(a,b,c)
                count += 1

count = 0
permute([1,2,3,4,5,6,7,8,9],0,8)

print(count)
print(sum(products))
# Euler Problem 24

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

permutations = []

# s = the string
# a = starting index
# b = ending index
def permute(s, a, b):
    if a==b:
        permutations.append(''.join([str(c) for c in s]))
    else:
        for i in range(a,b+1):
            s[a], s[i] = s[i], s[a]
            permute(s, a+1, b)
            s[a], s[i] = s[i], s[a] #backtrack

digits = "0123456789"
permute(list(digits), 0, len(digits)-1)

# sort numerically
permutations.sort()

# retrieve the millionth permutation
print(permutations[999999])
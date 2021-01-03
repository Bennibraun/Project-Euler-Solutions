# Euler Problem 34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math

f = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880
}

fdig = {
    0: 1,
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 5,
    9: 6
}

def get_oom(digits):
    max_digs = 0
    for i in digits:
        max_digs = max(max_digs, fdig[i])
    return max_digs

total = 0
for i in range(3, 50000):
    busted = False
    digits = [int(d) for d in str(i)]
    if abs(len(digits) - get_oom(digits)) < 2:        
        fact_sum = 0
        for d in digits:
            fact_sum += f[d]
            if fact_sum > i:
                busted = True
                break
        
        if not busted:
            if (fact_sum == i):
                total += fact_sum

print(total)
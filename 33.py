# Euler Problem 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import math

matches = []

for num in range(11, 100):
    for den in range(11, 100):
        num_dig = [num % 10, int(num / 10)]
        den_dig = [den % 10, int(den / 10)]
        if not ((0 in num_dig and 0 in den_dig) or (num_dig[0] == num_dig[1]) or (num == den) or (num > den)):
            d = 0
            for ni in range(0, 2):
                for di in range(0, 2):
                    if num_dig[ni] == den_dig[di]:
                        n = num_dig[abs(ni - 1)]
                        d = den_dig[abs(di - 1)]
            
            frac = num / den
            try:
                if n / d == frac:
                    matches.append([num, den])
            except:
                pass

def simplify(num, den):

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and den % i == 0:
            num /= i
            den /= i
    for i in range(2, int(math.sqrt(den)) + 1):
        if num % i == 0 and den % i == 0:
            num /= i
            den /= i
        
    return (num,den)

num_prod = 1
den_prod = 1
for f in matches:
    num_prod *= f[0]
    den_prod *= f[1]

print(simplify(num_prod,den_prod)[1])

# Euler Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import math

def isPrime(n):
    sqrt = (int)(math.sqrt(n)+1)
    for i in range(2,sqrt):
        if n%i==0:
            return False
    return True

def rotate(n):

    nstr = ''.join([str(x) for x in n])
    nstr = nstr[1:] + nstr[0]
    # print('nstr=',nstr)

    return nstr

# Start count at 1 to include 2 (skipping evens)
count = 1
for p in range(3,1000001,2):
    busted = False
    pl = [int(x) for x in str(p)]
    for i in range(0, len(pl)):
        # Convert int p to list to maintain zeroes
        pl = rotate(pl)

        # Convert rotated p back to int
        p = [str(x) for x in pl]
        p = int(''.join(p))

        # Check if the rotation yields prime
        if not isPrime(p):
            busted = True
            break

    if not busted:
        count += 1

print(count)
# Euler Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math


def isPrime(num):
    sqrt = (int)(math.sqrt(num)+1)
    for i in range(2,sqrt):
        if num%i==0:
            return False
    return True


prime_nums = []
for i in range(3,10000):
    if isPrime(i):
        prime_nums.append(i)


for p in prime_nums:
    if 600851475143 % p == 0:
        print(p)

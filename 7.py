# Euler Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


import math

def isPrime(num):
    sqrt = (int)(math.sqrt(num)+1)
    for i in range(2,sqrt):
        if num%i==0:
            return False
    return True

i = 3
primes = []

while len(primes) < 10001-1:
    if isPrime(i):
        primes.append(i)
    i += 1

print(primes[-1])

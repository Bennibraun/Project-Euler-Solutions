# Euler Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


import math

def isPrime(num):
    sqrt = (int)(math.sqrt(num)+1)
    for i in range(2,sqrt):
        if num%i==0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if isPrime(i):
        sum += i

print(sum)

# Euler Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


num = 2520

def isDivisible(num):
    for i in range(1,20):
        if num%i != 0:
            return False
    return True

while not (isDivisible(num)):
    num += 20
print(num)

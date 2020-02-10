# Euler Problem 20

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


factorial = 1
n = 100

for i in range(1,n+1):
    factorial *= i

factorial_digits = [int(x) for x in str(factorial)]
sum = 0

for i in factorial_digits:
    sum += i

print(sum)

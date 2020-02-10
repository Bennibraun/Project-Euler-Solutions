# Euler Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

i = 1
square_sum = 0
sum_square = 0

while i <= 100:
    square_sum += (i**2)
    sum_square += i
    i += 1

print((sum_square**2) - square_sum)
    

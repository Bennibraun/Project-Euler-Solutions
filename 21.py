# Euler Problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


def divisor_sum(num):
    sum = 0
    for i in range(1,(int)(num/2)+1):
        if num % i == 0:
            sum += i
    return sum


amicable_nums = []
for i in range(1,10000):
    a = divisor_sum(i)
    b = divisor_sum(a)
    if b == i and a != 0 and a not in amicable_nums and b not in amicable_nums and a != b:
        amicable_nums.append(a)
        amicable_nums.append(b)

print(amicable_nums)

amicable_sum = 0
for i in amicable_nums:
    amicable_sum += i

print(amicable_sum)

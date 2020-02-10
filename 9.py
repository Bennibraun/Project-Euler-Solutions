# Euler Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pyTriplet(n):
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if  (i**2) + (j**2) == (k**2):
                    if i + j + k == 1000:
                        return i*j*k
    return "not found. increase range"

print(pyTriplet(500))

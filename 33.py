# Euler Problem 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import math

product_num = 1
product_den = 1

for numerator in range(10,100):
    for denominator in range(numerator+1,100):
        # print numerator,
        # print '/',
        # print denominator
        quotient = float(numerator)/float(denominator)
        num_list = [float(x) for x in str(numerator)]
        den_list = [float(x) for x in str(denominator)]
        for i in range(0,2):
            for j in range(0,2):
                if num_list[0] != num_list[1] and num_list[0] != 0 and num_list[1] != 0 and den_list[j] != 0 and num_list[i] / den_list[j] == quotient and num_list[j] == num_list[i]:
                    print 'multiplying by ', numerator, ' and ', denominator
                    product_num *= numerator
                    product_den *= denominator

print product_num, '/', product_den

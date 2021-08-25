import math


def checkPandigital(a,b):
    n_str = ''
    for i in range(1,b+1):
        n_str += str(a*i)
        if len(n_str) > 9:
            return False
    if len(n_str) != 9:
        return False
    for i in range(1,10):
        if n_str.count(str(i)) != 1:
            return False
    return n_str

biggest_pandigital_number_found_so_far = 0
for i in range(1,10000):
    for j in range(1,10):
        pandig = checkPandigital(i,j)
        if pandig:
            print(i,':',j,':',pandig)
            if biggest_pandigital_number_found_so_far < int(pandig):
                biggest_pandigital_number_found_so_far = int(pandig)

print(biggest_pandigital_number_found_so_far)
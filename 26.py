# Euler Problem 26

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from decimal import *

# set precision of decimals. For this problem, min of 2000 is necessary.
setcontext(Context(prec=2000))

length = 0
completed = []

for d in range(1,1000):
    frac = Decimal(1) / Decimal(d)
    frac = list(str(frac))
    frac = frac[2:]
    if len(frac) > 8:
        # skip single-repeating decimals
        if frac[7] == frac[6] == frac[8] == frac[9] == frac[5]:
            pass
        else:
            for i in range(0,len(frac)):
                for j in range(i,len(frac)):
                    if d in completed:
                        break
                    # length shouldn't be below 6, might need adjustment for smaller implementations
                    if j-i > 6:
                        if frac[i:j] == frac[j:j+j-i] and frac[i:j] != ['0'] and frac[i:j] != []:
                            completed.append(d)
                            if j-i >= length:
                                longest_d = d
                                length = j-i
                            break
                if d in completed:
                    break

print('d=',longest_d,', len=',length)
# Euler Problem 31

# In the United Kingdom the currency is made up of pound and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p), and 2 pounds (200p).
# It is possible to make 2 pounds in the following way:
# 1*1 pound + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
# How many different ways can 2 pounds be made using any number of coins?



# Constant time, but shitty
# TODO: find a non-shitty way to do this

count = 0
print('1p','2p','5p','10p','20p','50p','100p','200p')

for p1 in range(0,201):
    for p2 in range(0,101):
        if 2*p2 + p1 <= 200:
            for p5 in range(0,41):
                if 5*p5 + 2*p2 + p1 <= 200:
                    for p10 in range(0,21):
                        if 10*p10 + 5*p5 + 2*p2 + p1 <= 200:
                            for p20 in range(0,11):
                                if 20*p20 + 10*p10 + 5*p5 + 2*p2 + 1*p1 <= 200:
                                    for p50 in range(0,5):
                                        if 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 + 1*p1 <= 200:
                                            for p100 in range(0,3):
                                                if 100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 + 1*p1 <= 200:
                                                    for p200 in range(0,2):
                                                        if p1+ (2*p2) + (5*p5) + (10*p10) + (20*p20) + (50*p50) + (100*p100) + (200*p200) == 200:
                                                            #print(p1,p2,p5,p10,p20,p50,p100,p200,' = 200')
                                                            count += 1
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break


print(count)
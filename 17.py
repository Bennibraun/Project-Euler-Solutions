# Euler Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


def single_letters(n):
    num_words = ['one','two','three','four','five','six','seven','eight','nine']
    if n <= 0 or n > 9:
        return 0
    else:
        return len(num_words[n-1])

def double_letters(n, m):
    if n < 0 or m < 0 or n > 9 or m > 9:
        return 0
    elif n == 0:
        return single_letters(m)
    elif n == 1:
        teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
        return len(teens[m-1])
    else:
        decas = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
        return len(decas[n-2]) + single_letters(m)


sum = 0
num = 0

for i in range(1,1001):
    n = [int(x) for x in str(i)]
    num += 1
    if i == 1000:
        sum += len('onethousand')
    elif i == 100:
        sum += len('onehundred')
    elif i > 100 and i % 100 == 0:
        sum += single_letters(n[0])
        sum += len('hundred')
    elif i > 100:
        sum += single_letters(n[0])
        sum += len('hundredand')
        sum += double_letters(n[1],n[2])
    elif i < 10:
        sum += single_letters(n[0])
    elif i < 100:
        sum += double_letters(n[0],n[1])
    else:
        print('unreachable state')
    
#Yes, I agree that this is kind of a bad algorithm. But it's also a silly problem.
print(sum)

import math

def divisors(n):
    div_list = [1]
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            if n/i==i:
                div_list.append(i)
            else:
                if (i not in div_list and int(n/i) not in div_list):
                    div_list.append(i)
                    div_list.append(int(n/i))
    return div_list

def is_abundant(n):
    sum = 0
    divs = divisors(n)
    for i in divs:
        sum += i
    return sum > n

def no_sum(n):
    for i in range(3,n):
        if is_abundant(i) and is_abundant(n-i):
            return False
    return True


non_abundant_sum = 0

for i in range(1,28123): #all ints afterward can be written as sum of 2 abundants
    if no_sum(i):
        non_abundant_sum += i

print(non_abundant_sum)
# takes a few minutes, could be better.
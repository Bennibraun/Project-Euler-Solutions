import math

# returns True if n is prime
def isPrime(n):
    sqrt = (int)(math.sqrt(n)+1)
    if n==1:
        return False
    for i in range(2,sqrt):
        if n%i==0:
            return False
    return True

# returns a list of the first n primes
def eratosthenes(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        sqrt = (int)(math.sqrt(i)+1)
        isPrime = True
        for j in range(2,sqrt):
            if i % j == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
        i += 1
    return primes

def isTruncatable(num):
    for i in range(len([d for d in str(num)])):
        #print('checking '+str(int(num/(10**i)))+' and '+str(int(num%(10**i))))
        if not isPrime(int(num/(10**i))) or not isPrime(int(num%(10**i))):
            return False
    return True

primes = eratosthenes(100000)
primes = [p for p in primes if p not in [2,3,5,7]]
print('primes generated')

truncatables = []
i = 0
while len(truncatables) < 11:
    p = primes[i]
    i += 1
    if isTruncatable(p):
        truncatables.append(p)

print(truncatables)
print(len(truncatables))
print(sum(truncatables))


# returns True if n is prime
def isPrime(n):
    sqrt = (int)(math.sqrt(n)+1)
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


# returns a list of divisors of n, incling 1, excluding n
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
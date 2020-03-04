
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


# finds all possible permutations of a list
# s = the list
# a = starting index
# b = ending index
def permute(s, a, b):
    if a==b:
        permutations.append(s)
    else:
        for i in range(a,b+1):
            s[a], s[i] = s[i], s[a]
            permute(s, a+1, b)
            s[a], s[i] = s[i], s[a] #backtrack


# Takes 3 ints, returns true iff there is exactly one instance of each digit from 1-9
def isPandigital(a, b, c):
    # Create list to track digit presence
    digits = [False for i in range(0,9)]

    # Turn ints into lists
    ints = [int(i) for i in (str(a) + str(b) + str(c))]
    
    for i in ints:
        if digits[i-1]:
            # Repeated digit found
            return False
        else:
            # Unique digit found
            digits[i-1] = True
    
    for i in digits:
        if not i:
            return False
    return True
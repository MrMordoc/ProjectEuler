def isPrime(number):
    isPrime = True
    for num in range(2, number/2):
        if number % num:
            isPrime = False
    return isPrime


def findPrime(x):
    primeNums = [2, 3, 5]
    i = 6
    while len(primeNums) < x:
        if isPrime(i):
            primeNums.append(i)
        i += 1
    return primeNums[-1]


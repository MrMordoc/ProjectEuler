numbers = range(2, 2000000)
primes = []
while len(numbers) > 0:
    primes.append(numbers[0])
    if len(primes) % 1000 == 0:
        print primes[-1]
    numbers = [x for x in numbers if x % numbers[0] != 0]

print sum(primes)

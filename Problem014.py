def collatzLength(n):
    m = n
    terms = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
        terms += 1
    return (m, terms)

maxLength = 0
longestNumber = 0
for n in range(1, 1000000):
    test = collatzLength(n)
    if test[1] > maxLength:
        maxLength = test[1]
        longestNumber = test[0]
        print test

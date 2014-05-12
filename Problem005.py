def lcmSeries(x):
    if x == 1:
        return 1
    else:
        return lcm(x, lcmSeries(x-1))

#calculates least common multiple of 2 items
def lcm(a, b):
    return ((a * b)/gcd(a, b))

#calculate greatest common divisor using Euclid's algorithm
def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)





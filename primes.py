import numpy
import math
def prime(upto=100):
    return filter(lambda num: (num % numpy.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))



def prime6(upto):
    primes = numpy.arange(3, upto + 1, 2)
    isprime = numpy.ones((upto-1)/2, dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return numpy.insert(primes[isprime],0,2)

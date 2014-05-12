import math

def latticePath(w, h):
    """w and h ints which represent the width and height of the lattice

    this algorithm uses combinations (n choose k) to compute paths through a lattice"""
    n = w + h
    k = n / 2
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

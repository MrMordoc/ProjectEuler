# sum of squares
def sumOfSquares(x):
    total = 0
    for num in range(x+1):
        total += num * num
    return total

# square of sums
def squareOfSums(x):
    subtotal = 0
    for num in range(x+1):
        subtotal += num
    total = subtotal * subtotal
    return total

def sumSquareDifference(x):
    return squareOfSums(x) - sumOfSquares(x)

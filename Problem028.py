#Number Spiral Diagonals

def findDiagonalSum(size):
	increment = 2
	nextNum = 1
	diagonalSum = 1
	while increment < size:
		for dummy_num in range(4):
			nextNum += increment
			diagonalSum += nextNum
		increment += 2
	return diagonalSum

print findDiagonalSum(3)
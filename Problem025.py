"""This program finds the first fibonacci term to contain n digits
this is for Project Euler problem 25"""

def first_fib_length(n):
	"""Takes an integer n and returns the first fibonacci number that
	has that many digits"""
	#define original terms
	x1 = 1
	x2 = 1
	#represents which Fibonacci term the current x2 is
	num = 2

	while len(str(x2)) < n:
		x3 = x1 + x2
		x1 = x2
		x2 = x3
		num += 1

	return num

print first_fib_length(1000)
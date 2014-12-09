"""finds the one millionth permutation in lexographic order of the digits 0 through 9
This is Project Euler problem 24"""

import itertools
perms = itertools.permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

count = 0
for item in perms:
	if count == 999999:
		num = ""
		for digit in item:
			num += digit
		print int(num)
		break
	else:
		count += 1
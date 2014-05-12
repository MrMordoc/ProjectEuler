import math

num = math.factorial(100)
num = str(num)
total = 0
for char in num:
    total += int(char)
print total

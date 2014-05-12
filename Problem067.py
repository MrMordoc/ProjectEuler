filename = "triangle.txt"
f = open(filename)
pyramid = f.read()
pyramid = pyramid.rstrip('\n')
pyramid = [[int(x) for x in y.split(' ')] for y in pyramid.split('\n')]

for i in range(len(pyramid)-2, -1, -1):
    for j in range(len(pyramid[i])):
        test1 = pyramid[i][j] + pyramid[i+1][j]
        test2 = pyramid[i][j] + pyramid[i+1][j+1]
        if test1 > test2:
            pyramid[i][j] = test1
        else:
            pyramid[i][j] = test2

print pyramid[0][0]

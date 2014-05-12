for x in range(100, 500):
    for y in range(100, 500):
        for z in range(100, 500):
            if x + y + z == 1000 and x**2 + y**2 == z**2:
                print x, y, z
                print x * y * z

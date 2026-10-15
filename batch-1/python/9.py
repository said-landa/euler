for a in range(1, 333):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if (c > b and c**2 == a**2 + b**2):
            print(a * b * c)
            
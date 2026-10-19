sideLen = 20
tableSize = sideLen + 1
ways = [
    [0 for column in range(tableSize)]
    for row in range(tableSize)
]
for column in range(tableSize):
    ways[0][column] = 1
for row in range(tableSize):
    ways[row][0] = 1 

for row in range(1, tableSize):
    for column in range(1, tableSize):
        above = ways[row - 1][column]
        left = ways[row][column - 1]
        value = above + left
        ways[row][column] = value


print(f"Number of ways is: {ways[sideLen][sideLen]}")

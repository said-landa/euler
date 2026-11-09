def sortLeastMost(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if (arr[minIndex] > arr[j]):
               minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

names = ['YEEZY', 'SAID', 'SALOME', 'JESUS']
scores = []

alphabet = {}
i = 1
for code in range(ord('A'), ord('Z') + 1):
    alphabet[(chr(code))] = i
    i += 1

for name in names:
    score = 0
    for ch in name:
        score += alphabet[ch]
    scores.append(score)

print(sortLeastMost(scores))
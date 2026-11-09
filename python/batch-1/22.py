names = ['SAID', 'SALOME', 'JESUS']

alphabet = {}
i = 1
for code in range(ord('A'), ord('Z') + 1):
    alphabet[(chr(code))] = i
    i += 1

print(alphabet)
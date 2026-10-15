def isPrime(num):
    numD = 0
    for i in range(2, num):
        if (num % i == 0):
            numD += 1
    if numD > 0:
        return False
    return True

primeC = 4
num = 10
numCopy = 0
units = [1,3,7,9]

while primeC < 10001:
    for i in units:
        numCopy = num
        numCopy += i
        if (isPrime(numCopy)):
            primeC += 1
            if primeC == 10001:
                print(primeC)
                print(numCopy)
    num += 10
    
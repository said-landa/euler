num = 600851475143
i = 2
primF = []

def divide(n, i):
    while (n % i == 0):
        n = n / i
    return n

while i <= num:
    if (num % i == 0):
        num = divide(num, i)
        primF.append(i)
    i += 1
        
print(primF)
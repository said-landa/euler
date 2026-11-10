#Largest Prime Factor

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

num = 1000
# num = 600851475143
i = 2 #we don't count 1 as prime.
primF = []

def divide(n, i):
    while (n % i == 0):
        n = n // i #we shrink the num as much as possible.
    return n

while i <= num:
    if (num % i == 0):
        num = divide(num, i)
        primF.append(i)
    i += 1
        
print(primF)
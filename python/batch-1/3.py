#Largest Prime Factor

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

num = 600851475143
i = 2 #we don't count 1 as prime.

def divide(n, i):
    while (n % i == 0):
        n = n // i #we shrink the num as much as possible.
    return n

while i * i <= num: #any prime factor num might have will be found -at most-, up to the square root of n, inclusive. math is beautiful.
    if (num % i == 0):
        num = divide(num, i)
    i += 1
        
print(num)
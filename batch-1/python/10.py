import math

bound = int(math.sqrt(2000000))
sum = 0

def isPrime(n):
  sRoot = int(math.sqrt(n))
  for i in range(2, sRoot + 1):
    if (n % i == 0):
      return False
  return True
  
for i in range(2, 2000000):
  if (isPrime(i)):
    sum += i

print(sum)
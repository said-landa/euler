import math

n = 1
i = 1
found = False

def getDivs(n):
  sqrN = math.isqrt(n)
  upN = math.ceil(sqrN)
  nD = 0
  for i in range(1, upN + 1):
    if (n == i):
      nD += 1
    if (n % i == 0):
      nD += 2

  return nD

while not found:
  n += i + 1
  if (getDivs(n) >= 500):
    found = True
    print(n)
  i += 1

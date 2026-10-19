number = 1000
m1 = 3
m2 = 5
sumA = 0

for i in range(1, number):
    if (i % 3 == 0 or i % 5 == 0):
        sumA += i
             
print(sumA)
  
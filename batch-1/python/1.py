number = 1000
m1 = 3
m2 = 5
arrayM = []

for i in range(1, number):
    if (i % 3 == 0 or i % 5 == 0):
        arrayM.append(i)
        
sumM = sum(arrayM)       
print(sumM)
  
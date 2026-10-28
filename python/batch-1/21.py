def newN(n):
    newN = 0
    for i in range(1, n):
        if (n % i == 0):
            newN += i
    return newN
            
 
sumFriends = 0
sumFrList = []

for a in range(4, 10000):
    b = newN(a)
    if (newN(b) == a and a != b):
        if (a not in sumFrList):
            print(f'Found {a} and {b}')
            sumFriends += a
            sumFriends += b
            sumFrList.append(a)
            sumFrList.append(b)
           
        
     
    
print(sumFriends)
    
num1 = 999
num2 = 998
lim = 899

def arePalin(num):
    revNum = num
    revNumArray = []
    while revNum > 0:
        revNumArray.append(revNum % 10)
        revNum //= 10
    for d in revNumArray:
        revNum = revNum * 10 + d
    if (revNum == num):
        return True
    return False
    

done = False
while num1 > lim and not done:
    while num2 > lim:
        prod = num1 * num2
        if(arePalin(prod)):
            print(num1, num2)
            done = True
            print(f"Biggest palindrome is {prod}")
            break
        else: 
            num2 -= 1
    if (num1 == lim + 1):
        lim = lim - 100
    num1 -= 1  
    num2 = num1 -1   
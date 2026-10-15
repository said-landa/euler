def diviByAll(prod, lim):
    for i in range(1, lim + 1):
        if not (prod % i == 0):
            return False
    return True
    
    

def squeeze(num, lim):
    stop = False
    while not stop:
        if(diviByAll(num, lim)):
            num //= 2
        else:
            num = num * 2
            stop = True
    return num
        

def calcNum(lim):
    num = lim
    while lim > 1:
        if (num % (lim - 1) == 0):
            lim -= 1
            continue
        num = num * (lim - 1)
        lim -= 1
    return num


lim = input('Enter limit: ')       
prod = calcNum(int(lim))
print(squeeze(prod, int(lim)))
num = 100
count = num
prod = 1

while count > 1:
    num = num * (count - 1)
    count -= 1

sum = 0
for i in str(num):
    sum += int(i)

print(sum)

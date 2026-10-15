base = 2
num = base ** 1000
sumA = 0
digits = [int(digit) for digit in str(num)]
for digit in digits:
    sumA += digit
print(f"Potencia: {1000}, número: {num}, suma: {sumA}")
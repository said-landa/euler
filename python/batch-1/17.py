letterCounts = {
    1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6,
    12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6,
    40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 10, 200: 10, 300: 12,
    400: 11, 500: 11, 600: 10, 700: 12, 800: 12, 900: 11, 1000: 11
}

def countLetters(number):
    numLetters = 0
    if number in letterCounts:
        numLetters = letterCounts[number]
        return numLetters
    else:
        numDigits = 0
        
        for i in str(number):
            numDigits += 1

        if numDigits > 2:
            numList = list(str(number))
            part = int((numList[0])) * 100
            numLetters += letterCounts[part] + 3
            numList.pop(0)
            if numList[0] == '0':
                numLetters += letterCounts[int(numList[1])]
                return numLetters

            number = int("".join(map(str, numList)))
            if number in letterCounts:
                numLetters += letterCounts[number]
                return numLetters
            else:
                part = (number // 10) * 10
                units = number % 10
                numLetters += letterCounts[part]
                numLetters += letterCounts[units]
                return numLetters
        
        part = (number // 10) * 10
        units = number % 10
        numLetters += letterCounts[part]
        numLetters += letterCounts[units]
        return numLetters

totalLetters = 0
for i in range(1, 1001):
    totalLetters += countLetters(i)

print(totalLetters)

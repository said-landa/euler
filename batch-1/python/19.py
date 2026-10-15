days = ['S', 'M', 'T', 'W', 'Th', 'F', 'Sa']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nSundays = 0
year = 1901
dayMonth = 1
monthCounter = 0
dayWeek = 2

while year < 2001:
    if year % 4 == 0:
        months[1] = 29
    else:
        months[1] = 28

    while monthCounter < 12:
        
        while dayMonth < months[monthCounter] + 1:
            if days[dayWeek] == 'S' and dayMonth == 1:
                nSundays += 1
    
            if dayWeek >= 6: 
                dayWeek = 0
            else: dayWeek += 1

            dayMonth += 1

        dayMonth = 1
        monthCounter += 1
       
    monthCounter = 0
    dayMonth = 1
    year += 1

print(nSundays)





    



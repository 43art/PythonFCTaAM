#Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит
#ip адрес, время и название дня недели (ex 139.18.150.126 23:12:44 sunday). Создайте
#новый текстовый файл, который будет содержать список ip адресов, наиболее популярный день
#недели, наиболее популярный отрезок времени длинною в один час. Последней строкой в файле
#добавьте наиболее популярный отрезок времени в сутках длинной один час в целом на сайте

file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

dictionaryIP = {}
dictionaryDays = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
dictionaryTime = {}

with file_input:
    firstLine = file_input.readline()
    listLine = firstLine.split()
    dictionaryIP.update({listLine[0]: 1})
    listTime = str(listLine[1]).split(':')
    dictionaryTime.update({listTime[0]: 1})
    for j in dictionaryDays.keys():
        if j == listLine[2]:
            count = dictionaryDays[j] + 1
            dictionaryDays.update({listLine[2]: count})
            break
    listLine.clear()
    listTime.clear()
    for line in file_input:
        listLine = line.split()
        flag = 0
        for j in dictionaryIP.keys():
            if j == listLine[0]:
                count = dictionaryIP[j] + 1
                dictionaryIP.update({listLine[0]: count})
                flag = 1
                break
        if flag == 0:
            dictionaryIP.update({listLine[0]: 1})
        listTime = str(listLine[1]).split(':')
        flag = 0
        for j in dictionaryTime.keys():
            if j == listTime[0]:
                count = dictionaryTime[j] + 1
                dictionaryTime.update({listTime[0]: count})
                flag = 1
                break
        if flag == 0:
            dictionaryTime.update({listTime[0]: 1})
        for j in dictionaryDays.keys():
            if j == listLine[2]:
                count = dictionaryDays[j] + 1
                dictionaryDays.update({listLine[2]: count})
                flag = 1
                break
        listLine.clear()
        listTime.clear()

with file_output:
    for key, val in dictionaryIP.items():
        file_output.write(str(key) + ' visited the site ' + str(val) + ' times\n')
    for key, val in dictionaryDays.items():
        file_output.write('On ' + str(key) + ' the number of visits ' + str(val) + '\n')
    popularTimeCount = 0
    for key, val in dictionaryTime.items():
        if popularTimeCount < val:
            popularTime = key
            popularTimeCount = val

    file_output.write('Most popular visiting time (hour) ' + str(popularTime) +
                      ' at this time the number of visits was ' + str(popularTimeCount) + ' times\n')
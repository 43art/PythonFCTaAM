#Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит
#ip адрес, время и название дня недели (ex 139.18.150.126 23:12:44 sunday). Создайте
#новый текстовый файл, который будет содержать список ip адресов, наиболее популярный день
#недели, наиболее популярный отрезок времени длинною в один час. Последней строкой в файле
#добавьте наиболее популярный отрезок времени в сутках длинной один час в целом на сайте

file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

dictionary = {}

with file_input:
    firstline = file_input.readline()
arrayLine = firstline.split()
dictionary.update({arrayLine[0]: 1})

file_input = open("input.txt", "r")
with file_input:
    for line in range(1):
        file_input.readline()
        arrayLines = file_input.readline()

print(arrayLines)


#dictionary.update({surname: vote})

#print(text)
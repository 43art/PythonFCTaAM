import csv
import pprint

def solve():
    inputFile = open('input.csv', 'r', encoding='utf-8')
    outputFile = open("output2.txt", "w")
    lines = [row for row in csv.reader(inputFile)]
    for line in range(1, len(lines)):
        performed = 0
        if lines[line][10] == '10,00' and lines[line][11] == '10,00':
            performed += 1
        if lines[line][12] == '10,00':
            performed += 1
        if lines[line][13] == '10,00' and lines[line][14] == '10,00':
            performed += 1
        if lines[line][15] == '10,00' and lines[line][16] == '10,00':
            performed += 1
        if lines[line][17] == '10,00' and lines[line][18] == '10,00' and lines[line][19] == '10,00':
            performed += 1
        if performed >= 2:
            outputFile.write(lines[line][0] + ' ' + lines[line][1] + '\n')
    inputFile.close()

solve()
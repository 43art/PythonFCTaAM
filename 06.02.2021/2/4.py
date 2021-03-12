l = list(map(int, input().split()))
extr = 0
length, maxLength = 0
for i in range(1, len(l) - 1):
    if (l[i-1] < l[i]) and (l[i] > l[i+1]):
        if (maxLength < length):
            maxLength = length
        length = 0
    else:
        length += 1
print(maxLength)
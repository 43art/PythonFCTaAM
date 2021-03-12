a = int(input())
b = -1
k = 0
max = 1
while(b != 0):
    b = int(input())
    if (a == b):
        k += 1
    else:
        if (max < k):
            max = k
        k = 1
    a = b
print(max)
a = int(input())
b = -1
k = 1
kk = 1
max = 1
while(b != 0):
    b = int(input())
    if (a < b):
        k += 1
    else:
        if (max < k):
            max = k
        k = 1
    if (a > b):
        kk += 1
    else:
        if (max < kk):
            max = kk
        kk = 1
    a = b
print(max)
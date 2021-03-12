l = list(map(int, input().split()))
extr = 0
for i in range(1, len(l) - 1):
    if (l[i-1] < l[i]) and (l[i] > l[i+1]):
        extr += 1
print(extr)
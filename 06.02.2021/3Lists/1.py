l = list(map(int, input().split()))
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (i == j):
            l.remove(j)
l.remove(1)
print(l)
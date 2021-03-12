A = int(input())
B = int(input())
for i in range(A, B):
    l = list(str(i))
    if (l == list(reversed(l))):
        for i in range(len(l)):
            l[i] = int(l[i])
        x = 0
        for i in range(len(l), 0, -1):
            x += 10 ** (i-1) * l[i-1]
        print(x)
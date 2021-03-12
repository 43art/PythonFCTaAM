N = int(input())
M = int(input())
dif = 0
l = []
for i in range(N):
    l.append(int(input()))
    l.sort()
for i in range(len(l)):
    dif += l[len(l)-1] - l[i]
if ((M - dif) % N == 0):
    solve = l[len(l)-1] + (M - dif) // N
else:
    solve = l[len(l) - 1] + (M - dif) // N + 1
print(solve)
A = int(input())
B = int(input())

for i in range(A, B):
    s = str(i)
    if (s.count(s[0]) == 3) or (s.count(s[1]) == 3):
        print(i)
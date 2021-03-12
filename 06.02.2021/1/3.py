def sum(k):
    sum1 = 0
    while (k > 0):
        sum1 += k % 10
        k //= 10
    return (sum1)

n = int(input())
for i in range(100, 1000):
    if (sum(i) == n):
        print(i)
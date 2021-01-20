N = int(input())
a = list(map(int, input().split()))

b = [0] * 4802
for x in a:
    b[x] += 1

mi = 0
for i in range(0, 2801, 400):
    if sum(b[i: i + 400]):
        mi += 1
ma = mi + sum(b[3200:])
mi = max(mi, 1)
print(mi, ma)
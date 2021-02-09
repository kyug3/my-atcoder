N, P = map(int, input().split())
A = list(map(int, input().split()))
o = [x for x in A if x % 2]
e = [x for x in A if not x % 2]

x = 0
num = 1
den = 1
for i, j in enumerate(range(len(e), 0, -1)):
    num *= j
    den *= i+1
    x += num // den


y = 0
num = 1
den = 1
for i, j in enumerate(range(len(o), 0, -1)):
    num *= j
    den *= i+1
    if (i+1) % 2 != P:
        continue
    else:
        y += num // den

if P == 0:
    print((x+1) * (y+1))
else:
    print((x+1) * y)
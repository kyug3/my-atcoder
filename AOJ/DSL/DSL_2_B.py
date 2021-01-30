def add(x, y):
    idx = x+n
    segt[idx] += y
    while True:
        idx //= 2
        if idx == 0:
            return 0
        segt[idx] += y

def getsum(x, y):
    l = x + n
    r = y + n
    s = 0
    while l < r:
        if l % 2 == 1:
            s += segt[l]
            l += 1
        l //= 2
        if r % 2 == 1:
            s += segt[r-1]
            r -= 1
        r //= 2
    return s


n, q = map(int, input().split())

segt = [0] * (n * 2 + 1)
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        add(x, y)
    else:
        print(getsum(x, y+1))

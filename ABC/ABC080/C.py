N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ma = float('-inf')
for i in range(2 ** 10):
    count = [0] * N
    frag = False
    for j in range(10):
        if (i >> j) & 1:
            for k, f in enumerate(F):
                if f[j] == 1:
                    count[k] += 1
                    frag = True
    if frag:
        total = 0
        for l, c in enumerate(count):
            total += P[l][c]
        ma = max(ma, total)
print(ma)
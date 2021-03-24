N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = float('-inf')
for i in range(2 ** 10):
    counts = []
    frag = False
    for f in F:
        c = 0
        for j in range(10):
            if (i >> j) & f[j]:
                c += 1
                frag = True
        counts.append(c)
    if frag:
        total = 0
        for n, x in enumerate(counts):
             total += P[n][x]
        ans = max(ans, total)
print(ans)
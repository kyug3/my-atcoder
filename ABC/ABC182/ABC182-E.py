import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
grid = [
    ['#'] * (W + 2) if i == 0 or i == H + 1 else
    ['#' if j == 0 or j == W + 1 else '.' for j in range(W + 2)]
    for i in range(H + 2)
]

for c, d in CD:
    grid[c][d] = '#'
for a, b in AB:
    grid[a][b] = 'A'

r = [[0] * (W + 2) for _ in range(H + 2)]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        g_status = grid[h][w]
        if g_status == 'A': r[h][w] = 1
        elif g_status == '.': r[h][w] = r[h][w - 1]

l = [[0] * (W + 2) for _ in range(H + 2)]
for h in reversed(range(1, H + 1)):
    for w in reversed(range(1, W + 1)):
        g_status = grid[h][w]
        if g_status == 'A': l[h][w] = 1
        elif g_status == '.':
            l[h][w] = l[h][w + 1]

d = [[0] * (W + 2) for _ in range(H + 2)]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        g_status = grid[h][w]
        if g_status == 'A': d[h][w] = 1
        elif g_status == '.': d[h][w] = d[h - 1][w]

u = [[0] * (W + 2) for _ in range(H + 2)]
for h in reversed(range(1, H + 1)):
    for w in reversed(range(1, W + 1)):
        g_status = grid[h][w]
        if g_status == 'A': u[h][w] = 1
        elif g_status == '.':
            u[h][w] = u[h + 1][w]
        
ans = 0
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if r[h][w] or l[h][w] or d[h][w] or u[h][w]:
            ans += 1
print(ans)
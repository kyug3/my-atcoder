import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(list(input().rstrip()))

R = [[0] * (W + 2) for _ in range(H + 2)]
D = [[0] * (W + 2) for _ in range(H + 2)]
for h in range(H):
    for w in range(W):
        if grid[h][w] == '.':
            R[h+1][w+1] = R[h+1][w] + 1
            D[h+1][w+1] = D[h][w+1] + 1
        else:
            R[h+1][w+1] = 0
            D[h+1][w+1] = 0

L = [[0] * (W + 2) for _ in range(H + 2)]
U = [[0] * (W + 2) for _ in range(H + 2)]
for h in reversed(range(H)):
    for w in reversed(range(W)):
        if grid[h][w] == '.':
            L[h+1][w+1] = L[h+1][w+2] + 1
            U[h+1][w+1] = U[h+2][w+1] + 1
        else:
            L[h+1][w+1] = 0
            U[h+1][w+1] = 0
ans = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        width = R[h][w] + L[h][w] - 1
        height = D[h][w] + U[h][w] - 1
        total = width + height - 1
        ans = max(ans, total)
print(ans)
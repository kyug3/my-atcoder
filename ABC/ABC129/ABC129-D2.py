import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]

R = [[0] * (W + 2) for _ in range(H + 2)]
D = [[0] * (W + 2) for _ in range(H + 2)]
L = [[0] * (W + 2) for _ in range(H + 2)]
U = [[0] * (W + 2) for _ in range(H + 2)]
for h in range(H):
    rh = H - h - 1
    for w in range(W):
        rw = W - w - 1
        if grid[h][w] == '.':
            R[h+1][w+1] = R[h+1][w] + 1
            D[h+1][w+1] = D[h][w+1] + 1
        else:
            R[h+1][w+1] = 0
            D[h+1][w+1] = 0
        if grid[rh][rw] == '.':
            L[rh+1][rw+1] = L[rh+1][rw+2] + 1
            U[rh+1][rw+1] = U[rh+2][rw+1] + 1
        else:
            L[rh+1][rw+1] = 0
            U[rh+1][rw+1] = 0
ans = 0
for h in range(1, H + 1):
    for w in range(1, W + 1):
        total = R[h][w] + L[h][w] + D[h][w] + U[h][w] - 3
        ans = max(ans, total)
print(ans)
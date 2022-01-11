import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N, C = li()
D = [li() for _ in range(C)]
grid = [li() for _ in range(N)]

iwakan = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        m = (i+j+2) % 3
        for c in range(C):
            iwakan[m][c] += D[grid[i][j]-1][c]

ans = INF
for i in range(C):
    x = iwakan[0][i]
    for j in range(C):
        if i == j:
            continue
        y = iwakan[1][j]
        for k in range(C):
            if i == k or j == k:
                continue
            z = iwakan[2][k]
            ans = min(ans, x+y+z)

print(ans)
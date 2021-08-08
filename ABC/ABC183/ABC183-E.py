import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

H, W = li()
grid = [list(input()) for _ in range(H)]

dp = [[0] * (W+2) for _ in range(H+2)]
tate = [[0] * (W+2) for _ in range(H+2)]
yoko = [[0] * (W+2) for _ in range(H+2)]
naname = [[0] * (W+2) for _ in range(H+2)]
dp[1][1] = 1
tate[1][1] = 1
yoko[1][1] = 1
naname[1][1] = 1

for h in range(1, H+1):
    for w in range(1, W+1):
        if grid[h-1][w-1] == '#' or h == w == 1:
            continue
        dp[h][w] = (tate[h-1][w] + yoko[h][w-1] + naname[h-1][w-1]) % mod
        tate[h][w] += tate[h-1][w] + dp[h][w]
        tate[h][w] %= mod
        yoko[h][w] += yoko[h][w-1] + dp[h][w]
        yoko[h][w] %= mod
        naname[h][w] += naname[h-1][w-1] + dp[h][w]
        naname[h][w] %= mod
        
print(dp[-2][-2])

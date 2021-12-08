import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

H, W = li()

grid = [list(input()) for _ in range(H)]
dir = ((1, 0), (0, 1), (1, 1))
dp = [[0] * (W+1) for _ in range(H+1)]

for h in range(H)[::-1]:
    for w in range(W)[::-1]:
        if grid[h][w] == '#':
            dp[h][w] = 0
            continue
        x = 1
        for i, j in dir:
            dh, dw = h + i, w + j
            if dp[dh][dw]:
                x = 0
        dp[h][w] = x

print('Second' if dp[0][0] else 'First')
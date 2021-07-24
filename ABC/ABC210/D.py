import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

H, W, C = li()
A = [li() for _ in range(H)]
dp = [[INF] * W for _ in range(H)]
ans = INF

for i in range(H)[::-1]:
    for j in range(W)[::-1]:
        x = C * (i+1 + j+1) + A[i][j]
        if i < H-1:
            dp[i][j] = min(dp[i][j], dp[i+1][j])
        if j < W-1:
            dp[i][j] = min(dp[i][j], dp[i][j+1])
        ans = min(ans, dp[i][j] - C*(i+1+j+1) + A[i][j])
        dp[i][j] = min(dp[i][j], x)

A = [a[::-1] for a in A]
dp = [[INF] * W for _ in range(H)]
for i in range(H)[::-1]:
    for j in range(W)[::-1]:
        x = C * (i+1 + j+1) + A[i][j]
        if i < H-1:
            dp[i][j] = min(dp[i][j], dp[i+1][j])
        if j < W-1:
            dp[i][j] = min(dp[i][j], dp[i][j+1])
        ans = min(ans, dp[i][j] - C*(i+1+j+1) + A[i][j])
        dp[i][j] = min(dp[i][j], x)
print(ans)
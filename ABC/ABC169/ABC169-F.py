import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
#mod = 10**9 + 7
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N, S = li()
A = li()

dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    a = A[i]
    for j in range(S+1):
        dp[i+1][j] += dp[i][j] * 2
        dp[i+1][j] %= mod
        if j + a <= S:
            dp[i+1][j+a] += dp[i][j]
            dp[i+1][j+a] %= mod

print(dp[N][S])
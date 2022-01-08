import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


N, K = li()
A = li()

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    a = A[i-1]
    for j in range(K+1):
        if dp[i-1][j]:
            dp[i][j] += dp[i-1][j]
            if j + a + 1 <= K:

                dp[i][j+a+1] -= dp[i-1][j]
    for j in range(1, K+1):
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= mod

print(dp[-1][K])
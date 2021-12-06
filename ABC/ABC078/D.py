import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, Z, W = li()
A = li()

dp = [[0] * (2) for _ in range(N+1)]

for i in range(N)[::-1]:
    if i == 0:
        dp[i][0] = abs(W - A[-1])
    else:
        dp[i][0] = abs(A[i-1] - A[-1])
        dp[i][1] = abs(A[i-1] - A[-1])
    for j in range(i+1, N):
        dp[i][0] = max(dp[i][0], dp[j][1])
        dp[i][1] = min(dp[i][1], dp[j][0])

print(dp[0][0])
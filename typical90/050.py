import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, L = li()
dp = [0] * (N+1)
dp[0] = 1

for i in range(N):
    if i + L > N:
        dp[i+1] += dp[i]
    else:
        dp[i+1] += dp[i]
        dp[i+L] += dp[i]
        dp[i+L] %= mod
    dp[i+1] %= mod

print(dp[-1])
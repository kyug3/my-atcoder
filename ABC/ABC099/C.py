import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + 1
    for j in range(1, N):
        if 6 ** j > i:
            break
        dp[i] = min(dp[i], dp[i - 6**j] + 1)
    for k in range(1, N):
        if 9 ** k > i:
            break
        dp[i] = min(dp[i], dp[i - 9**k] + 1)

print(dp[N])
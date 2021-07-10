import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from bisect import bisect_left

L = input()
N = len(L)

# j -> L未満が確定してるかどうか
dp = [[0] * 2 for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    if L[i] == '1':
        dp[i+1][1] += dp[i][0] + dp[i][1] * 3
        dp[i+1][0] += dp[i][0] * 2
    else: # L[i] == 0
        dp[i+1][1] += dp[i][1] * 3
        dp[i+1][0] += dp[i][0]
    dp[i+1][1] %= mod
    dp[i+1][0] %= mod
    
print((dp[-1][0] + dp[-1][1]) % mod)

import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

K = int(input())
if K % 9:
    print(0)
    exit()
dp = [0] * (K+1)
dp[0] = 1

for i in range(1, K+1):
    B = min(i, 9)
    for j in range(1, B+1):
        dp[i] += dp[i-j] % mod
print(dp[K] % mod)

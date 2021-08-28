import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

S = input()
N = len(S)
d = 1
mods = [0] * N
for i in range(N)[::-1]:
    mods[i] = int(S[i]) * d % 2019
    d *= 10
    d %= 2019


acc = [0] * (N+1)
for i in range(N):
    acc[i+1] = (acc[i] + mods[i]) % 2019

dp = [0] * 2019
dp[0] = 1
ans = 0
for i in range(1, N+1):
    ans += dp[acc[i]]
    dp[acc[i]] += 1
print(ans)
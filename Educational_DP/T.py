import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N = int(input())
S = list(input())

dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1

acc = [0] * (N+2)
acc[0] = 1
for i in range(1, N):
    s = S[i-1]
    if s == '>':
        for j in range(1, i+1):
            dp[i][j] = acc[j-1]
    else:
        for j in range(i):
            dp[i][j] = acc[i-1] - acc[j-1]
    acc[0] = dp[i][0]
    for j in range(1, i+1):
        acc[j] = (acc[j-1] + dp[i][j]) % mod

print(sum(dp[len(S)]) % mod)

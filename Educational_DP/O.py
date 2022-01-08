import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


N = int(input())
A = [li() for _ in range(N)]

dp = [0] * (1 << N)
dp[0] = 1

for st in range(1 << N):
    i = bin(st).count('1')
    for j in range(N):
        if (st >> j) & 1 or A[i][j] == 0:
            continue
        dp[st | (1 << j)] += dp[st]
        dp[st | (1 << j)] %= mod

print(dp[-1])
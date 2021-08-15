import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

K = input()
l = len(K)
D = int(input())
dp = [[[0] * D for _ in range(2)] for _ in range(l+1)]
dp[0][1][0] = 1

for i in range(l):
    for j in range(2):
        for k in range(D):
            for l in range(10):
                if j and int(K[i]) < l:
                    continue
                dp[i+1][j & (int(K[i]) == l)][(k+l) % D] += dp[i][j][k]
                dp[i+1][j & (int(K[i]) == l)][(k+l) % D] %= mod

print((dp[-1][0][0] + dp[-1][1][0] - 1) % mod)
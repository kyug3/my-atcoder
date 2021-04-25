import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())

N, ma, mb = n_inp()

dp = [[[float('inf')] * 401 for _ in range(401)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    a, b, c = n_inp()
    for j in range(401):
        for k in range(401):
            if dp[i][j][k] != float('inf'):
                dp[i+1][j+a][k+b] = min(dp[i][j][k]+c, dp[i+1][j+a][k+b])
                dp[i+1][j][k] = min(dp[i][j][k], dp[i+1][j][k])

ans = float('inf')
a = [i for i in range(ma, 401, ma)]
b = [i for i in range(mb, 401, mb)]
for i in range(1, N+1):
    for j, k in zip(a, b):
        ans = min(ans, dp[i][j][k])
print(-1 if ans == float('inf') else ans)
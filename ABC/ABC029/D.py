import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = input()
M = len(N)
dp = [[[0] * 2 for _ in range(12)] for _ in range(M+1)]

dp[0][0][1] = 1

for i in range(M):
    for j in range(11):
        for k in range(2):
            for l in range(10):
                if k and l > int(N[i]):
                    break
                if l == 1:
                    dp[i+1][j+1][k & (int(N[i]) == l)] += dp[i][j][k]
                else:
                    dp[i+1][j][k & (int(N[i]) == l)] += dp[i][j][k]
            
ans = 0
for j in range(11):
    ans += (dp[-1][j][0] + dp[-1][j][1]) * j
print(ans)

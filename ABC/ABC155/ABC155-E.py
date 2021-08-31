import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = list(input())
N = [int(i) for i in N]
dp = [[INF] * 2 for _ in range(len(N))]

dp[-1][0] = N[-1]
dp[-1][1] = 10 - N[-1]
for i in range(len(N)-1)[::-1]:
    dp[i][0] = min(dp[i+1][0] + N[i], dp[i+1][1] + N[i] + 1)
    dp[i][1] = min(dp[i+1][0] + (10 - N[i]), dp[i+1][1] + (10 - N[i] - 1))

ans = min(dp[0][0], dp[0][1] + 1)
print(ans)
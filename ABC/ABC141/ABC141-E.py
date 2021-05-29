import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))


N = int(input())
S = input().rstrip()

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(N)[::-1]:
    for j in range(N)[::-1]:
        if S[i] == S[j]:
            dp[i][j] = dp[i+1][j+1] +1

ans = 0
for i in range(N):
    for j in range(i+1, N):
        x = min(j-i, dp[i][j])
        ans = max(ans, x)

print(ans)

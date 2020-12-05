import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
dp = [-1 for _ in range(N+1)]
dp[0] = 1
for a in A:
    dp[a] = 0

for i in range(1, N+1):
    if dp[i] == 0:
        continue
    if i == 1:
        dp[1] = dp[0]
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[-1] % 1000000007)
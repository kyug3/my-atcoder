N = int(input())
S = [input().rstrip() for _ in range(N)]
dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(N):
    if S[i] == 'AND':
        dp[i+1][1] += dp[i][1]
        dp[i+1][0] += dp[i][1] + (dp[i][0] * 2)
    else:
        dp[i+1][1] += dp[i][0] + (dp[i][1] * 2)
        dp[i+1][0] += dp[i][0]
print(dp[-1][-1])
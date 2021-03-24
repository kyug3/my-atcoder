N = int(input())
P = list(map(float, input().split()))

# dp[i][j] i枚中j枚が表となる確率
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][1] = P[0]
dp[1][0] = 1 - P[0]

for i in range(2, N + 1):
    for j in range(i + 1):
        dp[i][j] += (
            dp[i-1][j-1] * P[i-1]
            + dp[i-1][j] * (1 - P[i-1])
        )
        
print(sum(dp[-1][(N+1)//2:]))
def chmin(dp, i, x):
    if x < dp[i]:
        dp[i] = x

def chmin_2d(dp, i, j, x):
    if x < dp[i][j]:
        dp[i][j] = x
        
import sys
input = sys.stdin.readline

s1 = input()
s2 = input()

dp = [[float('inf')] * (len(s2)+1) for _ in range(len(s1)+1)]
dp[0][0] = 0
for i in range(len(s1) + 1):
    for j in range(len(s2) + 1):
        if i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
print(dp[-1][-1])
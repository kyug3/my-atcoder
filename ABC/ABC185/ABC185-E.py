import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N + 1):
    if i == 0:
        for j in range(M + 1):
            dp[i][j] = j
    else:
        dp[i][0] = i

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            x = dp[i - 1][j - 1] + 1
            y = dp[i - 1][j] + 1
            z = dp[i][j - 1] + 1
            dp[i][j] = min(x, min(y, z))

print(dp[N][M])
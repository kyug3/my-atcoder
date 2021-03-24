N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N-1)]
dp[0][A[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        a = dp[i - 1][j]
        if a:
            x = j + A[i]
            y = j - A[i]
            if 0 <= x <= 20:
                dp[i][x] += a
            if 0 <= y <= 20:
                dp[i][y] += a
print(dp[-1][A[-1]])
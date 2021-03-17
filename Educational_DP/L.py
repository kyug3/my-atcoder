N = int(input())
A = list(map(int, input().split()))

# dp[l][r] l以上r未満の範囲のX-Yの最大値
dp = [[0] * (N+1) for _ in range(N+1)]

for width in range(1, N + 1):
    for left in range(N - width + 1):
        right = left + width
        if width % 2 == N % 2:
            dp[left][right] = max(
                dp[left+1][right] + A[left],
                dp[left][right-1] + A[right-1]
            )
        else:
            dp[left][right] = min(
                dp[left+1][right] - A[left],
                dp[left][right-1] - A[right-1]
            )

print(dp[0][N])
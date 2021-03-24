N = int(input())
R = [0] * N
C = [0] * N
for i in range(N):
    R[i], C[i] = map(int, input().split())

dp = [[0] * N for _ in range(N)]
for i in range(1, N):
    for l in range(N - i):
        r = i + l
        dp[l][r] = 10 ** 9        
        for mid in range(l, r):
            dp[l][r] = min(dp[l][r], dp[l][mid] + dp[mid+1][r] + R[l]*C[mid]*C[r])
print(dp[0][-1])
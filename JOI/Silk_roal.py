N, M = map(int, input().split())
dist = [int(input()) for _ in range(N)]
weather = [int(input()) for _ in range(M)]

dp = [[float('inf')] * (M + 1) if n else [0] * (M + 1) for n in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i, M + 1):
        dp[i][j] = min(dp[i-1][:j]) + dist[i-1] * weather[j-1]

print(min(dp[-1]))
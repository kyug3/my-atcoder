N, M = map(int, input().split())
dist = [int(input()) for _ in range(N)]
weather = [int(input()) for _ in range(M)]

dp = [[float('inf')] * (M + 1) if n else [0] * (M + 1) for n in range(N + 1)]

for i in range(1, N + 1):
    mins = [float('inf')] * (i + 1)
    for j in range(i, M + 1):
        if i == 1:
            dp[i][j] = dist[i-1] * weather[j-1]
        else:
            dp[i][j] = last_mins[j] + dist[i-1] * weather[j-1]
        mins.append(min(mins[-1], dp[i][j]))
    last_mins = mins.copy()

print(min(dp[-1]))
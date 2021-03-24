N = int(input())
xyz = [list(map(int, input().split())) for _ in range(N)]

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + max(0, b[2] - a[2])

dist = [[distance(xyz[i], xyz[j]) for i in range(N)] for j in range(N)]
dp = [[float('inf')] * N for _ in range(2 ** N)]
dp[1][0] = 0
for i in range(2 ** N):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            dp[i|(1<<k)][k] = min(dp[i|(1<<k)][k], dp[i][j] + dist[j][k])
print(dp[2**N - 1][0])
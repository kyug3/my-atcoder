import sys
input = sys.stdin.readline

N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('inf') for _ in range(10**5 + 1)] for n in range(N+1)]

for i in range(1, N+1):
    w = WV[i-1][0]
    v = WV[i-1][1]
    for j in range(1, 10**5+1):
        if j == v:
            dp[i][j] = min(dp[i-1][j], w)
        elif j > v:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v] + w)
        else:
            dp[i][j] = dp[i-1][j]

for n, x in enumerate(reversed(dp[-1])):
    if x <= W:
        print(10**5 - n)
        break
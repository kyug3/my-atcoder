import sys
input = sys.stdin.readline

D, N = map(int, input().split())
temp = [int(input()) for _ in range(D)]
clothes = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(D)]

for i in range(D):
    t = temp[i]
    for j in range(N):
        if not (clothes[j][0] <= t <= clothes[j][1]):
            continue
        elif i == 0:
            dp[i][j] = 0
            continue
        for k in range(N):
            if dp[i-1][k] == -1:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(clothes[j][2] - clothes[k][2]))

print(max(dp[-1]))
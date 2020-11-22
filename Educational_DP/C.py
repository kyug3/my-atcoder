import sys
input = sys.stdin.readline

N = int(input())
a, b, c = [], [], []
for _ in range(N):
    x, y, z = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)

dp = [[0] * 3 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(3):
        if j == 0:
            dp[i][0] = max(dp[i-1][1] + a[i-1], dp[i-1][2] + a[i-1])
        elif j == 1:
            dp[i][1] = max(dp[i-1][0] + b[i-1], dp[i-1][2] + b[i-1])
        else:
            dp[i][2] = max(dp[i-1][0] + c[i-1], dp[i-1][1] + c[i-1])
print(max(dp[-1][0] , max(dp[-1][1], dp[-1][2])))

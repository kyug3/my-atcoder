H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
mod = 10 ** 9 + 7

dp = [[0] * W for _ in range(H)]
flag = False
for w in range(W):
    if grid[0][w] == '#':
        flag = True
    if flag:
        dp[0][w] = 0
    else:
        dp[0][w] = 1
flag = False
for h in range(H):
    if grid[h][0] == '#':
        flag = True
    if flag:
        dp[h][0] = 0
    else:
        dp[h][0] = 1

for h in range(1, H):
    for w in range(1, W):
        if grid[h][w] == '#':
            dp[h][w] = 0
            continue
        dp[h][w] = (dp[h-1][w] + dp[h][w-1]) % mod
print(dp[-1][-1])
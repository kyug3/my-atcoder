H, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

# dp[i] 残り体力iの時の最小の消費MP
dp = [float('inf')] * (H + 1)
dp[0] = 0

for h in range(1, H + 1):
    for a, b in AB:
        if h - a >= 0:
            dp[h] = min(dp[h], dp[h-a] + b)
        else:
            dp[h] = min(dp[h], b)

print(dp[-1])

import sys
import numpy as np
input = sys.stdin.readline

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()
dp = np.zeros(T+1, dtype=np.int64)
ans = 0
for a, b in AB:
    ans = max(ans, dp[-2] + b)
    dp[a:] = np.maximum(dp[:-a] + b, dp[a:])

print(ans)
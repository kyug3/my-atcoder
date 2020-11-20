import numpy as np
 
N, W = map(int, input().split())
 
dp = np.zeros(W+1, dtype=np.int64)
 
for _ in range(N):
    w, v = map(int,input().split())
    np.maximum(dp[:-w]+v, dp[w:], out=dp[w:])
 
print(dp[-1])
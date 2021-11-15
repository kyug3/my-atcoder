import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

H, W = li()
A = [li() for _ in range(H)]
B = [li() for _ in range(H)]
dif = [[0] * (W+1) for _ in range(H+1)]
for h in range(H):
    for w in range(W):
        dif[h][w] = abs(A[h][w] - B[h][w])

dp = [[set() for _ in range(W + 1)] for _ in range(H + 1)]
dp[0][0].add(dif[0][0])

for h in range(H):
    for w in range(W):
        for i in dp[h][w]:
            d1 = dif[h+1][w]
            dp[h+1][w].add(i + d1)
            dp[h+1][w].add(abs(i - d1))

            d2 = dif[h][w+1]
            dp[h][w + 1].add(i + d2)
            dp[h][w + 1].add(abs(i - d2))

ans = min(dp[H-1][W-1])

print(ans)
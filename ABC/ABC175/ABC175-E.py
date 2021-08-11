import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

H, W, K = li()
V = [[0] * (W+1) for _ in range(H+1)]
for _ in range(K):
    h, w, v = li()
    V[h][w] = v

last = [[0] * 4 for _ in range(W+1)]

for h in range(1, H+1):
    now = [[0] * 4 for _ in range(W+1)]
    for w in range(1, W+1):
        # 下方向
        now[w][0] = max(last[w])
        now[w][1] = now[w][0] + V[h][w]

        now[w][0] = max(now[w-1][0], now[w][0])
        for i in range(1, 4):
            now[w][i] = max(now[w-1][i], now[w][i])
            now[w][i] = max(now[w-1][i-1] + V[h][w], now[w][i])
    last = now

print(max(now[-1]))
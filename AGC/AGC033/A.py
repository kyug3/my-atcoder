import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

H, W = li()
grid = [input() for _ in range(H)]
blacks = []
seen = [[0] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if grid[h][w] == '#':
            seen[h][w] = 1
            blacks.append((h, w))

dq = deque(blacks)
ans = 0
while dq:
    h, w = dq.popleft()
    for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        dh = h + i
        dw = w + j
        if dh < 0 or dw < 0 or dh >= H or dw >= W or seen[dh][dw]:
            continue
        seen[dh][dw] = seen[h][w] + 1
        ans = max(ans, seen[dh][dw] - 1)
        dq.append((dh, dw))

print(ans)

import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

N, M = li()
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = li()
    u -= 1; v -= 1
    G[u].append(v)
S, T = li()
S -= 1; T -= 1

seen = [INF] * N
seen[S] = 0
seen2 = [[0] * N for _ in range(4)]
def kenken(start):
    ret = []
    dq = deque()
    dq.append((start, 0))
    while dq:
        x, c = dq.pop()
        for y in G[x]:
            if seen2[c+1][y]:
                continue
            seen2[c+1][y] = 1
            if c == 2:
                if seen[y] > seen[start] + 1:
                    seen[y] = seen[start] + 1
                    ret.append(y)
            else:
                dq.append((y, c+1))
    return ret

nxt = deque([S])
while nxt:
    x = nxt.popleft()
    if seen2[0][x]:
        continue
    seen2[0][x] = 1
    nxt += kenken(x)

if seen[T] == INF:
    seen[T] = -1
print(seen[T])
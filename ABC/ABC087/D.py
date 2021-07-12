import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

N, M = li()
edges = [[] for _ in range(N)]
redges = [[] for _ in range(N)]
seen = [0] * N
for _ in range(M):
    l, r, d = li()
    l -= 1
    r -= 1
    edges[l].append((r, d))
    redges[r].append((l, d))
    seen[l] = seen[r] = 1

stack = deque()
for i in range(N):
    if not redges[i]:
        stack.append(i)
INF = float('inf')
dist = [INF] * N
while stack:
    x = stack.pop()
    for y, d in edges[x]:
        if dist[x] == INF:
            if dist[y] == INF:
                dist[x] = 0
                dist[y] = d
            else:
                dist[x] = dist[y] - d
        elif dist[y] == INF:
            dist[y] = dist[x] + d
        else:
            if dist[x] == dist[y] - d:
                continue
            else:
                print('No')
                exit()
        stack.append(y)
for i in range(N):
    if seen[i]:
        if dist[i] == INF:
            print('No')
            exit()
print('Yes')
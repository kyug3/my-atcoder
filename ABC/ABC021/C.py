import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

N = int(input())
a, b = li()
a -= 1; b -= 1
M =  int(input())
edges = [[] for _ in range(N)]
for _ in range(M):
    x, y = li()
    x -= 1; y -= 1
    edges[x].append(y)
    edges[y].append(x)

deq = deque([a])
dist = [[INF, 0] for _ in range(N)]
dist[a] = [1, 1]
while deq:
    x = deq.popleft()
    d, c = dist[x]
    for y in edges[x]:
        if dist[y][0] > d + 1:
            deq.append(y)
        if dist[y][0] >= d + 1:
            dist[y][0] = d + 1
            dist[y][1] += c
            dist[y][1] %= mod

print(dist[b][1])
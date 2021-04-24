import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def g_inp(N, M):
    g = [[] for _ in range(N)]
    for _ in range(M):
        a, b, z = map(int, input().split())
        a -= 1; b -= 1
        g[a].append((z, b))
        g[b].append((z, a))
    return g
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())

import heapq

N, M = n_inp()
AB = [[] for _ in range(10**5+1)]
for _ in range(N):
    a, b = n_inp()
    AB[a-1].append(-b)

h = []
heapq.heapify(h)
ans = 0
for i in range(M):
    for j in AB[i]:
        heapq.heappush(h, j)
    if len(h):
        ans -= heapq.heappop(h)

print(ans)

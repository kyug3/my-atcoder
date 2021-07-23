import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

N, M = li()
A = [0] * N
ab = [[] for _ in range(N)]
for _ in range(M):
    a, b = li()
    a -= 1; b -= 1
    ab[a].append(b)
    ab[b].append(a)

for i in range(N):
    deq = deque([i])
    dist = [-1] * N
    dist[i] = 0
    ans = 0
    while deq:
        x = deq.popleft()
        for y in ab[x]:
            if dist[y] >= 0:
                continue
            dist[y] = dist[x] + 1
            if dist[y] == 2:
                ans += 1
            deq.append(y)
    print(ans)
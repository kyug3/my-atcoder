import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque
INF = float('inf')

def bfs(start, num_node, graph):
    queue = deque([start])
    seen = [INF] * (num_node)
    seen[start] = 0
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if seen[y] < INF:
                continue
            seen[y] = seen[x] + 1
            queue.append(y)
    return seen

N, M = li()
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = li()
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

K = int(input())
C = li()
C = [i-1 for i in C]
dists = [[] for _ in range(K)]
for i in range(K):
    lst = bfs(C[i], N, G)
    for c in C:
        dists[i].append(lst[c])

dp = [[INF] * K for _ in range(2**K)]
for i in range(K):
    dp[1 << i][i] = 1

for i in range(2**K):
    for j in range(K):
        for k in range(K):
            if j == k: continue
            if (1 << k) & i: continue
            dp[i | (1<<k)][k] = min(dp[i | (1<<k)][k], dp[i][j] + dists[j][k])

ans = INF
for i in dp[-1]:
    ans = min(ans, i)
ans = -1 if ans == INF else ans
print(ans)
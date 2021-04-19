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


N, M = n_inp()

def dfs_with_stack(start, num_node, graph):
    stack = [start]
    while stack:
        x = stack.pop()
        seen[x] = True
        for z2, y in graph[x]:
            if seen[y]:
                continue
            stack.append(y)

G = g_inp(N, M)
seen = [False] * N
ans = 0
for i in range(N):
    if seen[i]: continue
    if G[i] == []:
        ans += 1
        continue
    ans += 1
    dfs_with_stack(i, N, G)
print(ans)
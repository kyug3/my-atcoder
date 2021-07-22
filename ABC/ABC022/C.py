import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
INF = float('inf')


N, M = li()
G1 = [[INF] * N for _ in range(N)]
G2 = [[INF] * N for _ in range(N)]
adj = []
for _ in range(M):
    u, v, l = li()
    u -= 1; v -= 1
    G1[u][v] = l
    G1[v][u] = l
    if u > 0 and u > 0:
        G2[u][v] = l
        G2[v][u] = l
    if u == 0:
        adj.append(v)
    if v == 0:
        adj.append(u)
def wf(g):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    return g

G2 = wf(G2)
ans = INF
for i in range(len(adj)):
    x = adj[i]
    for j in range(i+1, len(adj)):
        y = adj[j]
        ans = min(ans, G2[x][y] + G1[0][x] + G1[0][y])
print(-1 if ans == INF else ans)
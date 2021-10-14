import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, M, L = li()
am = [[0 if i == j else INF for j in range(N)]
      for i in range(N)]

for _ in range(M):
    a, b, c = li()
    a -= 1; b -= 1
    am[a][b] = c
    am[b][a] = c

def floyd_warshall(num_node, am):
    # am = adjacency matrix
    for k in range(num_node):
        for i in range(num_node):
            for j in range(num_node):
                am[i][j] = min(am[i][j], am[i][k] + am[k][j])
    return am

dists = floyd_warshall(N, am)
for i in range(N):
    for j in range(N):
        if dists[i][j] <= L:
            dists[i][j] = 1
        else:
            dists[i][j] = INF

dists = floyd_warshall(N, dists)

for _ in range(int(input())):
    s, t = li()
    s -= 1; t -= 1
    ans = dists[s][t]
    if ans == INF:
        ans = -1
    else:
        ans -= 1
    print(ans)
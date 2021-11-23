import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    x, y = li() 
    x -= 1; y -= 1
    G[x].append(y)
    G[y].append(x)

def preprocess(G, N):
    dq = deque([0])
    dist = [-1] * N
    par = [[0] * (N.bit_length()+1) for _ in range(N)]
    dist[0] = 0
    while dq:
        x = dq.popleft()
        for y in G[x]:
            if dist[y] >= 0:
                continue
            dq.append(y)
            dist[y] = dist[x] + 1
            par[y][0] = x
    
    for i in range(1, N.bit_length() + 1):
        for j in range(N):
            par[j][i] = par[par[j][i-1]][i-1]

    return dist, par

def LCA(x, y, dist, par, N):
    if dist[x] > dist[y]:
        x, y = y, x
    for i in range(N.bit_length() + 1):
        if (dist[y] - dist[x]) >> i & 1:
            y = par[y][i]
    
    if x == y:
        return x

    for i in range(N.bit_length())[::-1]:
        if par[x][i] != par[y][i]:
            x = par[x][i]
            y = par[y][i]
    return par[x][0]

dist, par = preprocess(G, N)

for _ in range(int(input())):
    a, b = li()
    a -= 1; b -= 1
    lca = LCA(a, b, dist, par, N)
    print(dist[a] + dist[b] - dist[lca]*2 + 1)
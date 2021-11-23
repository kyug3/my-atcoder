import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

def bellman_ford(edges, start, N):
    dist = [-INF] * N
    dist[start] = 0
    cnt = 0
    negative_loop = 0
    while 1:
        cnt += 1
        update = 0
        for now in range(N):
            for c, next in edges[now]:
                if dist[next] < dist[now] + c:
                    dist[next] = dist[now] + c
                    update = 1
        if not update:
            break
        if cnt == N:
            negative_loop = 1
            break
    while 1:
        cnt += 1
        update = 0
        for now in range(N):
            for c, next in edges[now]:
                if dist[next] < dist[now] + c:
                    dist[next] = INF
                    update = 1
        if not update:
            break
        if cnt == N:
            negative_loop = 1
            break
    
    return dist, negative_loop



N, M, P = li()
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = li()
    u -= 1; v -= 1; c -= P
    G[u].append((c, v))

d, n = bellman_ford(G, 0, N)
if d[N-1] == INF:
    print(-1)
else:
    print(max(0, d[N-1]))

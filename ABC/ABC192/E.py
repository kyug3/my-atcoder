import sys
input = sys.stdin.readline
import heapq


def dijkstra(graph, num_node, start):
    hq = [(0, start)]
    heapq.heapify(hq)
    distance = [float('inf')] * (num_node + 1)
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for d, n, k in graph[node]:
            if distance[node] % k != 0:
                d += k - (distance[node] % k)
            now_dist = d + distance[node]
            if now_dist < distance[n]:
                distance[n] = now_dist
                heapq.heappush(hq, (now_dist, n))
    return distance[Y]

N, M, X, Y = map(int, input().split())
X -= 1; Y -= 1
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = map(int, input().split())
    A -= 1; B -= 1
    G[A].append((T, B, K))
    G[B].append((T, A, K))

ans = dijkstra(G, N, X)
print(-1 if ans == float('inf') else ans)
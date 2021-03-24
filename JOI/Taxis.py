import sys
import heapq
from collections import deque
input = sys.stdin.readline

def dijkstra(s, g):
    hq = [(0, s)]
    heapq.heapify(hq)
    distance = [float('inf')] * (N + 1)
    distance[s] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for n in g[node]:
            d = CR[node-1][1]
            now_dist = d + distance[node]
            if distance[n] > now_dist:
                distance[n] = now_dist
                heapq.heappush(hq, (now_dist, n))
    return distance


N, K = map(int, input().split())
CR = [[i + 1] + list(map(int, input().split())) for i in range(N)]
graph = [[] for _ in range(N + 1)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

new_graph = [[] for _ in range(N + 1)]
for i, c, r in CR:
    queue = deque([i])
    seen = [0] * (N + 1)
    seen[i] = 1
    while queue:
        x = queue.popleft()
        if seen[x] > r:
            continue
        for y in graph[x]:
            if seen[y]:
                continue
            seen[y] = seen[x] + 1
            queue.append(y)
    seen = [i for i, j in enumerate(seen) if j]
    for s in seen:
        if s == i:
            continue
        new_graph[i].append(s)
dist = dijkstra(1, new_graph)
print(dist[N])
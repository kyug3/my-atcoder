import sys
import heapq
from collections import deque
input = sys.stdin.readline

def dijkstra(start, graph):
    hq = [(0, start)]
    heapq.heapify(hq)
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for d, n in graph[node]:
            temp = d + distance[node]
            if temp < distance[n]:
                distance[n] = temp
                heapq.heappush(hq, (temp, n))
    return distance

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
zombie = []
for _ in range(K):
    zombie.append(int(input()))
graph = [[] for _ in range(N + 1)]
AB = [list(map(int, input().split())) for _ in range(M)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)

danger = [0] * (N + 1)
for z in zombie:
    queue = deque([z])
    temp_danger = [0] * (N + 1)
    temp_danger[z] = 1
    while queue:
        x = queue.popleft()
        if temp_danger[x] >= S + 1:
            continue
        for i in graph[x]:
            if temp_danger[i]:
                continue
            temp_danger[i] = temp_danger[x] + 1
            queue.append(i)
    danger = [max(a, b) for a, b in zip(danger, temp_danger)]

w_graph = [[] for _ in range(N + 1)]
zombie = set(zombie)
for a, b in AB:
    if a in zombie or b in zombie:
        continue
    if b == N:
        w_graph[a].append((0, b))
    elif danger[b]:
        w_graph[a].append((Q, b))
    else:
        w_graph[a].append((P, b))

    if a == N:
        w_graph[b].append((0, a))
    elif danger[a]:
        w_graph[b].append((Q, a))
    else:
        w_graph[b].append((P, a))

dists = dijkstra(1, w_graph)
print(dists[N])
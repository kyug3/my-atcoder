N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N):
    lst = list(map(int, input().split()))
    u, k = lst[0], lst[1]
    lst = lst[2:]
    for i in range(0, len(lst), 2):
        v, c = lst[i], lst[i+1]
        graph[u].append((c, v))

import heapq

def dijkstra(graph, num_node, start):
    hq = [(0, start)]
    heapq.heapify(hq)
    distance = [float('inf')] * num_node
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for d, n in graph[node]:
            now_dist = d + distance[node]
            if now_dist < distance[n]:
                distance[n] = now_dist
                heapq.heappush(hq, (now_dist, n))
    return distance

dists = dijkstra(graph, N, 0)
for i in range(N):
    print(i, dists[i])
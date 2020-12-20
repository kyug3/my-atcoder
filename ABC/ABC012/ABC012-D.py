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
        for n, d in graph[node]:
            temp = d + distance[node]
            if temp < distance[n]:
                distance[n] = temp
                heapq.heappush(hq, (temp, n))
    return distance

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((b, t))
    G[b].append((a, t))

ans = float("inf")
for n in range(N):
    ans = min(ans, max(dijkstra(G, N, n)))
print(ans)
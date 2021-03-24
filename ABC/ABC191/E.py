import heapq


def dijkstra(graph, num_node, start):
    hq = [(0, start)]
    heapq.heapify(hq)
    distance = [float('inf')] * (num_node + 1)
    distance[start] = 0
    ans = float('inf')
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for d, n in graph[node]:
            now_dist = d + distance[node]
            if now_dist < distance[n]:
                distance[n] = now_dist
                heapq.heappush(hq, (now_dist, n))
            if n == start:
                ans = min(ans, now_dist)
    return ans

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
loop = [float('inf')] * N
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1; B -= 1
    if A == B:
        loop[A] = min(loop[A], C)
    else:
        graph[A].append((C, B))

for i in range(N):
    ans = min(dijkstra(graph, N, i), loop[i])
    print(-1 if ans == float('inf') else ans)
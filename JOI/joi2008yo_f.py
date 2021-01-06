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

N, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
ans = []
for _ in range(K):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        c, d, e = inp[1:]
        graph[c].append((d, e))
        graph[d].append((c, e))
    else:
        a, b = inp[1:]
        dists = dijkstra(graph, N + 1, a)
        x = dists[b]
        if x == float('inf'):
            x = -1
        ans.append(x)

for a in ans:
    print(a)
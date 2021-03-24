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
        for d, n in graph[node]:
            now_dist = d + distance[node]
            if now_dist < distance[n]:
                distance[n] = now_dist
                heapq.heappush(hq, (now_dist, n))
    return distance
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
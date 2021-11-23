import heapq


def dijkstra(graph, num_node, start):
    hq = [(0, start)]
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


def dijkstra(graph, num_node, start):
    """
    経路復元するよう
    """
    hq = [(0, start, -1)]
    distance = [float('inf')] * num_node
    used = [0] * num_node
    prev = [-1] * num_node
    distance[start] = 0

    while hq:
        dist, node, pre = heapq.heappop(hq)
        if used[node]:
            continue
        used[node] = 1
        prev[node] = pre
        for d, n in graph[node]:
            now_dist = d + distance[node]
            if now_dist < distance[n]:
                distance[n] = now_dist
                heapq.heappush(hq, (now_dist, n, node))

    return distance, prev

def get_path(t, prev):
    """
    prevを作ったときの始点から点tへの最短距離の経路
    """
    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    path = path[::-1]
    return path

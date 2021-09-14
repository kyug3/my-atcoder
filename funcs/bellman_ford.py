INF = float('inf')


def bellman_ford(edges, start, N):
    dist = [INF] * N
    dist[start] = 0
    cnt = 0
    negative_loop = 0
    while 1:
        cnt += 1
        update = 0
        for now in range(N):
            for c, next in edges[now]:
                if dist[next] > dist[now] + c:
                    dist[next] = dist[now] + c
                    update = 1
        if not update:
            break
        if cnt == N:
            negative_loop = 1
            break
    return dist, negative_loop

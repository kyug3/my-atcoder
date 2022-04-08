def tree_dia(G):
    """
    木の直径に含まれる頂点の列挙
    """
    from collections import deque

    N = len(G)

    def bfs(start):
        """
        dist: startからi番目の頂点の距離
        idx: startから最も離れた頂点
        """

        dist = [0] * N
        idx = start
        dist[start] = 1
        dq = deque((start,))
        while dq:
            x = dq.popleft()
            d = dist[x]
            idx = x
            for y in G[x]:
                if dist[y]:
                    continue
                dist[y] = d + 1
                dq.append(y)
        return dist, idx

    _, fr = bfs(0)
    dist, x = bfs(fr)

    dia = [x]
    while x >= 0:
        for y in G[x]:
            if dist[y] + 1 == dist[x]:
                x = y
                dia.append(x)
                break
        else:
            break

    return dia
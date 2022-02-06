from collections import deque

def toposort(G, rG, N):
    deg = [0] * N
    q = deque()
    topo = []
    for i in range(N):
        if len(rG[i]) == 0:
            q.append(i)
        else:
            deg[i] = len(rG[i])

    while q:
        x = q.popleft()
        topo.append(x+1)
        for y in G[x]:
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)
    return topo

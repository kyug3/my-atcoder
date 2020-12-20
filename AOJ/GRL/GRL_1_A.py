import sys
import heapq
input = sys.stdin.readline

V, E, r = map(int, input().split())
d = [-1 for _ in range(V)]

def dijkstra(start: int):
    hq = [(0, start)]
    heapq.heapify(hq)
    distance = [float('inf')] * V
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for n, d in G[node]:
            temp = d + distance[node]
            if temp < distance[n]:
                distance[n] = temp
                heapq.heappush(hq, (temp, n))
    return distance

G = [[] for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    G[s].append((t, d))
    #G[t].append((s, d))

for x in dijkstra(r):
    if x == float("inf"):
        print("INF")
    else:
        print(x)
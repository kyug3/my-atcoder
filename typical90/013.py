import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

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
        for d, n in graph[node]:
            now_dist = d + distance[node]
            if now_dist < distance[n]:
                distance[n] = now_dist
                heapq.heappush(hq, (now_dist, n))
    return distance

N, M = li()
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = li()
    A -= 1; B -= 1
    graph[A].append((C, B))
    graph[B].append((C, A))

dist1 = dijkstra(graph, N, 0)
dist2 = dijkstra(graph, N, N-1)

for i in range(N):
    ans = dist1[i] + dist2[i]
    print(ans)
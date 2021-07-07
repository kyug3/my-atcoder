import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import deque

N = int(input())
AB = []
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = li()
    a -= 1
    b -= 1
    AB.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, num_node):
    queue = deque([start])
    seen = [0] * (num_node)
    seen[start] = 1
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if seen[y]:
                continue
            seen[y] = seen[x] + 1
            queue.append(y)
    return seen

depth = bfs(0, N)

C = [0] * N
Q = int(input())
for _ in range(Q):
    t, e, x = li()
    a, b = AB[e-1]
    if t == 2:
        a, b = b, a
    if depth[a] < depth[b]:
        C[0] += x
        C[b] -= x
    else:
        C[a] += x

def bfs2(start, num_node):
    queue = deque([start])
    seen = [0] * (num_node)
    seen[start] = 1
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if seen[y]:
                continue
            C[y] += C[x]
            seen[y] = seen[x] + 1
            queue.append(y)
    return C
bfs2(0, N)
for c in C:
    print(c)

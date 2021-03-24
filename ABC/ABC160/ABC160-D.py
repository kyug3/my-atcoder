import sys
from collections import deque
input = sys.stdin.readline

N, X, Y = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(1, N):
    graph[i].append(i + 1)
    graph[i + 1].append(i)
graph[X].append(Y)
graph[Y].append(X)

count = [0] * (N + 1)
def bfs(start, seen):
    queue = deque([start])
    seen[start] = 1
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if seen[y]:
                continue
            queue.append(y)
            seen[y] = seen[x] + 1
            count[seen[y] - 1] += 1

for i in range(1, N + 1):
    seen = [0] * (N + 1)
    bfs(i, seen)
    
for c in count[1:-1]:
    print(c // 2)
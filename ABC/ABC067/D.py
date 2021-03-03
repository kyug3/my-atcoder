from collections import deque

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

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

F = bfs(0, N)
S = bfs(N-1, N)
f_cnt = 0
s_cnt = 0

for f, s in zip(F, S):
    if f <= s:
        f_cnt += 1
    else:
        s_cnt += 1

if f_cnt > s_cnt:
    print('Fennec')
else:
    print('Snuke')
from collections import deque

def dfs(n, parent):
    for x in G[n]:
        if x == parent:
            continue
        dfs(x, n)

def dfs_with_stack(start, num_node):
    stack = [start]
    seen = [False] * (num_node + 1)
    while stack:
        x = stack.pop()
        seen[x] = True
        for y in graph[x]:
            if seen[y]:
                continue
            stack.append(y)

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
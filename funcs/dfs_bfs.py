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

def dfs_with_stack(start, num_node):
    queue = deque([start])
    seen = [False] * (num_node + 1)
    while queue:
        x = queue.popleft()
        seen[x] = True
        for y in graph[x]:
            if seen[y]:
                continue
            queue.append(y)
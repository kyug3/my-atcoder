from collections import deque

def dfs(n, parent):
    for x in G[n]:
        if x == parent:
            continue
        dfs(x, n)

def dfs_with_stack(start, num_node):
    stack = [start]
    seen = [False] * (num_node + 1)
    seen[start] = True
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if seen[y]:
                continue
            stack.append(y)
            seen[y] = True

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


def grid_bfs(sh, sw):
    queue = deque(((sh, sw),))
    seen = [[-1] * W for _ in range(H)]
    seen[sh][sw] = 0
    while queue:
        last_h, last_w = queue.popleft()
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            h = last_h + i
            w = last_w + j
            if h >= H or w >= W or h < 0 or w < 0:
                continue
            if seen[h][w] >= 0 or grid[h][w] == '#':
                continue
            seen[h][w] = seen[last_h][last_w] + 1
            queue.append((h, w))
    return seen
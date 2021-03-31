from collections import deque

def bfs(sh, sw):
    queue = deque(((sh, sw),))
    seen = [[-1] * W for _ in range(H)]
    seen[sh][sw] = 1
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
    return seen[H-1][W-1]

H, W = map(int, input().split())
grid = []
black = 0
for _ in range(H):
    line = list(input())
    grid.append(line)
    for w in range(W):
        if line[w] == '#':
            black += 1

x = bfs(0, 0)
print(-1 if x == -1 else H*W - x - black)
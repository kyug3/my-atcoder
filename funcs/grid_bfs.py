H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

from collections import deque

def bfs(sh, sw):
    dq = deque(((sh, sw),))
    seen = [[-1] * W for _ in range(H)]
    seen[sh][sw] = 0
    while dq:
        h, w = dq.popleft()
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh = h + i
            nw = w + j
            if nh >= H or nw >= W or nh < 0 or nw < 0:
                continue
            if seen[nh][nw] >= 0 or grid[nh][nw] == '#':
                continue
            seen[nh][nw] = seen[h][w] + 1
            dq.append((nh, nw))
    return seen


    
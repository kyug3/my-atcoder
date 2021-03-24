from collections import deque

H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

grid = [[0] * W for _ in range(H)]
queue = deque([(0, 0)])
cnt = 0
color = 0
while queue:
    h, w = queue.pop()
    grid[h][w] = color + 1
    cnt += 1
    if A[color] == cnt:
        color += 1
        if color == N:
            break
        cnt = 0
    for i, j in ((1,0), (-1,0), (0,1), (0,-1)):
        nexth = h + i
        nextw = w + j
        if nexth >= H or nextw >= W or nexth < 0 or nextw < 0:
            continue
        if grid[nexth][nextw]:
            continue
        queue.append((nexth, nextw))

for x in grid:
    print(*x)
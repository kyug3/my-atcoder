from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

queue = deque([(0,0)])
seen = [[10 ** 5] * W for _ in range(H)]
seen[0][0] = 0 if grid[0][0] == '.' else 1
while queue:
    h, w = queue.popleft()
    for i, j in ((0, 1), (1, 0)):
        next_h = h + i
        next_w = w + j
        if next_h >= H or next_w >= W or next_h < 0 or next_w < 0:
            continue
        if grid[next_h][next_w] == '.':
            if seen[h][w] < seen[next_h][next_w]:
                seen[next_h][next_w] = seen[h][w]
                queue.append((next_h, next_w))
        else:
            if grid[h][w] == '#':
                if seen[h][w] < seen[next_h][next_w]:
                    seen[next_h][next_w] = seen[h][w]
                    queue.append((next_h, next_w))
                
            else:
                if seen[h][w] < seen[next_h][next_w]:
                    seen[next_h][next_w] = seen[h][w] + 1
                    queue.append((next_h, next_w))

print(seen[-1][-1])
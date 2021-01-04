import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
dic = {chr(c): [] for c in range(ord('a'), ord('z') + 1)}
grid = [list(input().rstrip()) for _ in range(H)]
for h in range(H):
    for w in range(W):
        status = grid[h][w]
        if status.islower():
            dic[status].append([h, w])
        elif status == 'S':
            sh, sw = h, w
        elif status == 'G':
            gh, gw = h, w

seen = [[0] * W for _ in range(H)]
queue = deque([[sh, sw]])
hmove = [1, -1, 0, 0]
wmove = [0, 0, 1, -1]
seen[sh][sw] = 1
while queue:
    i, j = queue.popleft()
    if grid[i][j] in dic:
        for h, w in dic[grid[i][j]]:
            if not seen[h][w]:
                seen[h][w] = seen[i][j] + 1
                queue.append([h, w])
        del dic[grid[i][j]]
    for n in range(4):
        h, w = hmove[n] + i, wmove[n] + j
        if 0 > h or h >= H or 0 > w or w >= W or grid[h][w] == '#':
            continue
        if not seen[h][w]:
            seen[h][w] = seen[i][j] + 1
            queue.append([h, w])
        
print(seen[gh][gw] - 1)
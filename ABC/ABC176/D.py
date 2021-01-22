import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
sh -= 1; sw -= 1; gh -= 1; gw -= 1

maze = [list(input().rstrip()) for _ in range(H)]

# 01BFS
dist = [[float('inf')] * W for _ in range(H)]
dist[sh][sw] = 0
queue = deque([(sh, sw)])
while queue:
    h, w = queue.popleft()
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i == j == 0:
                continue
            h2 = h + i
            w2 = w + j
            if h2 < 0 or w2 < 0 or h2 >= H or w2 >= W or maze[h2][w2] == '#':
                continue
            # 歩き
            if (((i == 1 or i == -1) and j == 0) 
                or ((j == 1 or j == -1) and i == 0)):
                if dist[h][w] >= dist[h2][w2]:
                    continue
                dist[h2][w2] = dist[h][w]
                queue.appendleft((h2, w2))
            # ワープ
            else:
                if dist[h][w] + 1 >= dist[h2][w2]:
                    continue
                dist[h2][w2] = dist[h][w] + 1
                queue.append((h2, w2))

ans = dist[gh][gw]
print(ans if ans != float('inf') else -1)
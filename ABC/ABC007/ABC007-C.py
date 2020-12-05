import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

maze = [list(input().rstrip()) for _ in range(R)]
seen = [[-1 for _ in range(C)] for _ in range(R)]
seen[sy-1][sx-1] = 0

def can_go(r, c):
    lst = []
    if maze[r-1][c] != "#" and seen[r-1][c] == -1:
        lst.append([r-1, c])
        seen[r-1][c] = seen[r][c] + 1
    if maze[r+1][c] != "#" and seen[r+1][c] == -1:
        lst.append([r+1, c])
        seen[r+1][c] = seen[r][c] + 1
    if maze[r][c-1] != "#" and seen[r][c-1] == -1:
        lst.append([r, c-1])
        seen[r][c-1] = seen[r][c] + 1
    if maze[r][c+1] != "#" and seen[r][c+1] == -1:
        lst.append([r, c+1])
        seen[r][c+1] = seen[r][c] + 1
    return lst

queue = deque([[sy-1, sx-1]])   
while True:
    if not queue:
        break
    x = queue.popleft()
    lst = can_go(x[0], x[1])
    for l in lst:
        queue.append(l)

print(seen[gy-1][gx-1])

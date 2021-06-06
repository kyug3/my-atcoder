import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import deque

H, W = li()
rs, cs = li()
rs -= 1; cs -= 1
rt, ct = li()
rt -= 1; ct -= 1
grid = [list(input().rstrip()) for _ in range(H)]

def grid_bfs(sh, sw):
    queue = deque(((sh, sw, 'X', 0),))
    seen = [[10 ** 9] * W for _ in range(H)]
    seen[sh][sw] = 0
    l1 = [1, -1, 0, 0]
    l2 = [0, 0, 1, -1]
    d = ['R', 'L', 'D', 'U']
    while queue:
        last_h, last_w, direction, cost = queue.popleft()
        for i in range(4):
            h = last_h + l1[i]
            w = last_w + l2[i]
            if h >= H or w >= W or h < 0 or w < 0:
                continue
            if grid[h][w] == '#':
                continue

            # 方向転換なし
            if d[i] == direction or direction == 'X':
                if seen[h][w] < cost:
                    continue
                seen[h][w] = cost
                queue.appendleft((h, w, d[i], cost))
            # あり
            else:
                if seen[h][w] < cost + 1:
                    continue
                seen[h][w] = cost + 1
                queue.append((h, w, d[i], cost+1))

    return seen

s = grid_bfs(rs, cs)
print(s[rt][ct])
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

H, W = map(int, input().split())
maze = []
seen = [[False for _ in range(W)] for _ in range(H)]
start, goal = False, False
for h in range(H):
    inp = list(input().rstrip())
    if not start:
        if "s" in inp:
            start = (h, inp.index("s"))
    if not goal:
        if "g" in inp:
            goal = (h, inp.index("g"))
    maze.append(inp)

def dfs(h, w):
    if h < 0 or H <= h or w < 0 or W <= w or maze[h][w] == "#":
        return None
    if seen[h][w]:
        return None
    seen[h][w] = True
    dfs(h+1, w)
    dfs(h-1, w)
    dfs(h, w+1)
    dfs(h, w-1)

dfs(start[0], start[1])
if seen[goal[0]][goal[1]]:
    print("Yes")
else:
    print("No")
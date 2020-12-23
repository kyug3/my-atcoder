import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N + 1)]
colors = {}
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    colors[(a, b)] = 0

def dfs(n, parent, parent_color):
    color = 1
    for x in G[n]:
        if x == parent:
            continue
        if color == parent_color:
            color += 1
        colors[(n, x)] = color
        dfs(x, n, color)
        color += 1
dfs(1, 0, -1)

print(max(colors.values()))
for c in colors.values():
    print(c)

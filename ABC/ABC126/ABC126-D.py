import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

bw = [0 for _ in range(N + 1)]
def dfs(x, parent):
    for d in G[x]:
        n, w = d[0], d[1]
        if parent == n:
            continue
        if w % 2 == 1:
            if bw[x] == 1:
                bw[n] = 0
            else:
                bw[n] = 1
        else:
            if bw[x] == 1:
                bw[n] = 1
            else:
                bw[n] = 0
        dfs(n, x)
dfs(1, -1)
for x in bw[1:]:
    print(x)
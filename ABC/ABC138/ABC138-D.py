import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, Q = map(int, input().split())
G = [[] for _ in range(N + 1)]
G[1].append(0)
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

values = [0 for _ in range(N + 1)]
for _ in range(Q):
    p, x = map(int, input().split())
    values[p] += x

def dfs(n, parent):
    for x in G[n]:
        if x == parent:
            continue
        values[x] += values[n]
        dfs(x, n)
dfs(1, 0)
print(' '.join(map(str, values[1:])))
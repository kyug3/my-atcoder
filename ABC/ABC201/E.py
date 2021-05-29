import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = li()
    u -= 1; v -= 1
    G[u].append((w, v))
    G[v].append((w, u))

dist = [0] * N

def dfs(start, num_node, graph=G):
    stack = [(start, -1),]
    seen = [False] * (num_node + 1)
    while stack:
        x, parent = stack.pop()
        seen[x] = True
        for w, y in graph[x]:
            if y == parent:
                continue
            dist[y] = w ^ dist[x]
            stack.append((y, x))

dfs(0, N)

ans = 0
for i in range(60):
    x = 0
    y = 0
    for j in range(N):
        if (dist[j] >> i) & 1:
            x += 1
            ans += y * (2**i)
        else:
            y += 1
            ans += x * (2**i)
        ans %= mod

print(ans)
import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = li()
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

ma = [-1, -1]
def dfs(n, parent):
    global ma
    for x in G[n]:
        if x == parent:
            continue
        dists[x] = dists[n] + 1
        if ma[0] < dists[x]:
            ma = (dists[x], x)
        dfs(x, n)

dists = [0] * N
dfs(0, -1)
dists = [0] * N
dfs(ma[1], -1)
print(ma[0]+1)
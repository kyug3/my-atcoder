import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
P = li()
G = [[] for _ in range(N)]
for e, i in enumerate(P):
    e += 1; i -= 1
    G[e].append(i)
    G[i].append(e)

depths = [[] for _ in range(N)]
in_ = [0] * N
out_ = [0] * N
count = 0
def dfs(n, parent, depth):
    global count
    count += 1
    depths[depth].append(count)
    in_[n] = count
    for x in G[n]:
        if x == parent:
            continue
        dfs(x, n, depth + 1)
    count += 1
    out_[n] = count

dfs(0, -1, 0)

import bisect
for _ in range(int(input())):
    u, d = li()
    u -= 1
    left = in_[u]
    right = out_[u]
    x = bisect.bisect_left(depths[d], left)
    y = bisect.bisect(depths[d], right)
    print(y - x)

import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

# https://atcoder.jp/contests/abc010/tasks/abc010_4

N, G, E = li()
p = li()
G = [[] for _ in range(N+1)]
for _ in range(E):
    fm, to = li()
    cap = 1
    forward = [to, cap, 0]
    forward[2] = backward = [fm, 0, forward]
    G[fm].append(forward)
    G[to].append(backward)

    fm, to = to, fm
    forward = [to, cap, 0]
    forward[2] = backward = [fm, 0, forward]
    G[fm].append(forward)
    G[to].append(backward)

for i in p:
    forward = [N, 1, 0]
    forward[2] = backward = [i, 0, forward]
    G[i].append(forward)
    G[N].append(backward)

used = [0] * N
def dfs(v, t, f):
    if v == t:
        return f
    used[v] = 1
    for e in G[v]:
        to, cap, rev = e
        if used[to] or cap <= 0:
            continue
        d = dfs(to, t, min(f, cap))
        if d > 0:
            e[1] -= d
            rev[1] += d
            return d
    return 0

def max_flow(s, t):
    global used
    flow = 0
    while 1:
        used = [0] * (N+1)
        f = dfs(s, t, INF)
        if f == 0:
            return flow
        flow += f

print(max_flow(0, N))
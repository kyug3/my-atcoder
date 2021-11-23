import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None
 
    def add_link(self, _from, to, cap):
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])
 
    def bfs(self, s):
        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        self.depth = depth
 
    def dfs(self, v, t, flow):
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0
 
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, INF)
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, INF)

def inside(x, y):
    return 0 <= x < N and 0 <= y < N

N = int(input())
C = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (i + j) % 2:
            if C[i][j] == 'B':
                C[i][j] = 'W'
            elif C[i][j] == 'W':
                C[i][j] = 'B'

d = Dinic(N**2 + 3)
s = N ** 2 + 1
t = s + 1
tot = N * (N-1) * 2
for i in range(N):
    for j in range(N):
        idx = i * N + j
        if C[i][j] == 'B':
            d.add_link(s, idx, INF)
        elif C[i][j] == 'W':
            d.add_link(idx, t, INF)

        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            di, dj = i + x, j + y
            didx = di * N + dj
            if inside(di, dj):
                d.add_link(idx, didx, 1)

print(tot - d.max_flow(s, t))

import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

N = int(input())
G = [[] for _ in range(N)]
AB = []
for _ in range(N-1):
    a, b = li()
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
    AB.append((a, b))

count = [-1] * N
start = -1
for i in range(N):
    if len(G[i]) == 1:
        count[i] = 1
    elif start == -1:
        start = i

def dfs(x, parent):
    if count[x] != -1:
        return count[x]
    c = 0
    for y in G[x]:
        if parent == y:
            continue
        c += dfs(y, x)
    count[x] = c + 1
    return c + 1
        
dfs(start, -1)
ans = 0
for a, b in AB:
    x, y = count[a], count[b]
    if y > x:
        x, y = y, x
    ans += y * (N-y)
print(ans)
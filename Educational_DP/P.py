import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque


N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = li()
    x -= 1; y -= 1
    edges[x].append(y)
    edges[y].append(x)

# 0: black, 1: white
seen = [0] * N
seen[0] = 1
dp = [[0] * 2 for _ in range(N)]
def f(x):
    flag = 1
    bl, wh = 1, 1
    for y in edges[x]:
        if seen[y]: 
            continue
        seen[y] = 1
        b, w = f(y)
        bl *= w
        wh *= (w + b)
        bl %= mod
        wh %= mod
        flag = 0
    if flag:
        return 1, 1
    dp[x][0] = bl % mod
    dp[x][1] = wh % mod
    return dp[x][0], dp[x][1]

a, b = f(0)
print((a + b) % mod)

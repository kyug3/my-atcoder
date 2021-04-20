import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def g_inp(N, M):
    g = [[] for _ in range(N)]
    for _ in range(M):
        a, b, z = map(int, input().split())
        a -= 1; b -= 1
        g[a].append((z, b))
        g[b].append((z, a))
    return g
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())


N, K = n_inp()
V = l_inp()
rV = V[::-1]
V2 = sorted(V)
sv = sum(V)
ans = 0
for k in range(1, K+1):
    x = 0
    if k >= N:
        x = sv - sum(V2[:K-k])
        ans = max(x, ans)
        continue
    for i in range(k+1):
        x = 0
        lst = []
        for j in range(i):
            x += V[j]
            if V[j] < 0:
                lst.append(V[j])
        for l in range(k-i):
            x += rV[l]
            if rV[l] < 0:
                lst.append(rV[l])
        lst.sort()
        x -= sum(lst[:K-k])
        ans = max(x, ans)

print(ans)
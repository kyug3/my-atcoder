import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M = li()
p = li()

def find(x):
    # xの根を求める
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x, y):
    # xとyが属する集合の併合
    x, y = find(x), find(y)
    if x == y:
        return None
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

def size(x):
    # xが属する集合の要素数
    return -par[find(x)]

def members(x):
    # xが属する集合に含まれる要素のリスト
    root = find(x)
    return [i for i in range(N) if find(x) == root]

par = [-1] * N
for i in range(M):
    x, y = li()
    x -= 1; y -= 1
    union(x, y)

ans = 0
for i in range(N):
    a = p[i]
    if find(a-1) == find(i):
        ans += 1

print(ans)
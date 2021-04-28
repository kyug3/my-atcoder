import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())

N = int(input())
XY = [[i] + l_inp() for i in range(N)]
xy1 = sorted(XY, key=lambda x: x[1])
xy2 = sorted(XY, key=lambda x: x[2])

edge = []
for i in range(N-1):
    edge.append((xy1[i][0], xy1[i+1][0], xy1[i+1][1] - xy1[i][1]))
    edge.append((xy2[i][0], xy2[i+1][0], xy2[i+1][2] - xy2[i][2]))

edge.sort(key=lambda x: x[2])

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

par = [-1] * N
ans = 0
for i in range(len(edge)):
    x, y, cost = edge[i]
    if find(x) == find(y):
        continue
    union(x, y)
    ans += cost

print(ans)
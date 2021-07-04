import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

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

N, M = li()
ABY = []
for _ in range(M):
    a, b, y = li()
    a -= 1; b -= 1
    ABY.append((a, b, y))
Q = int(input())
VW = []
for i in range(Q):
    v, w = li()
    v -= 1
    VW.append((v, w, i))
VW.sort(reverse=True, key=lambda x: x[1])
ABY.sort(reverse=True, key=lambda x: x[2])

par = [-1] * N

idx = 0
ans = [0] * Q
for a, b, y in ABY:
    while idx < Q and VW[idx][1] >= y:
        ans[VW[idx][2]] = size(VW[idx][0])
        idx += 1
    union(a, b)

for i in range(idx, Q):
    ans[VW[i][2]] = size(VW[i][0])

for i in ans:
    print(i)
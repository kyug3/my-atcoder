import sys
from collections import defaultdict
input = sys.stdin.readline

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
    for k, v in clas[y].items():
        clas[x][k] += v
    par[y] = x

N, Q = map(int, input().split())
C = list(map(int, input().split()))
par = [-1] * N
clas = [defaultdict(int) for _ in range(N)]
for i, c in enumerate(C):
    clas[i][c] += 1

for _ in range(Q):
    q, a, b = map(int, input().split())
    a -= 1
    if q == 1:
        b -= 1
        union(a, b)
    else:
        print(clas[find(a)][b])
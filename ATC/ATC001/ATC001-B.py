import sys
input = sys.stdin.readline

def find(x):
    if par[x] == -1:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return None
    if rank[x] > rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[y] += 1
    par[x] = y

N, Q = map(int, input().split())
par = [-1] * N
rank = [1] * N

for _ in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        unite(a, b)
    elif p == 1:
        if find(a) == find(b):
            print("Yes")
        else:
            print("No")

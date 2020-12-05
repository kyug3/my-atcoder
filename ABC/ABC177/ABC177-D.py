import sys
input = sys.stdin.readline

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return None
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

def size(x):
    return -par[find(x)]

N, M = map(int, input().split())
par = [-1] * N
ans = 0
for m in range(M):
    a, b = map(int, input().split())
    unite(a-1, b-1)
for n in range(N):
    ans = max(ans, size(n))
print(ans)

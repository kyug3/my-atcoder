N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
par = [-1] * N

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

ans = 0
for i in range(M):
    par = [-1] * N
    for j in range(M):
        if i == j:
            continue
        a, b = E[j]
        a -= 1; b -= 1
        unite(a, b)
    if size(0) != N:
        ans += 1
print(ans)
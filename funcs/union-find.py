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

N = int(input())
par = [-1] * N
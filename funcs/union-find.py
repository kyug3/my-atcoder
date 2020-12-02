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

N = int(input())
par = [-1] * N
rank = [1] * N
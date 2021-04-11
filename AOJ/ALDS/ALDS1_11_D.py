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

N, M = map(int, input().split())
par = [-1] * N
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print('yes' if find(a) == find(b) else 'no')
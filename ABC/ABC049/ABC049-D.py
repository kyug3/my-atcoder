import sys
input = sys.stdin.readline

def find(x, par):
    # xの根を求める
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x], par)
        return par[x]

def union(x, y, par):
    # xとyが属する集合の併合
    x, y = find(x, par), find(y, par)
    if x == y:
        return None
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

N, K, L = map(int, input().split())
road = [-1] * N
train = [-1] * N

for _ in range(K):
    p, q = map(int, input().split())
    p -= 1; q -= 1
    union(p, q, road)
for _ in range(L):
    r, s = map(int, input().split())
    r -= 1; s -= 1
    union(r, s, train)

pars = {}
lst = []
for i in range(N):
    k = str(find(i, road)) + ' ' + str(find(i, train))
    if k in pars:
        pars[k] += 1
    else:
        pars[k] = 1
    lst.append(k)
ans = []
for k in lst:
    ans.append(pars[k])
print(*ans)
import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M, K = li()

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

par = [-1] * N
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = li()
    a -= 1; b -= 1
    friends[a].append(b)
    friends[b].append(a)
    union(a, b)

block = [0] * N
for _ in range(K):
    c, d = li()
    c -= 1; d -= 1
    if find(c) == find(d):
        block[c] += 1
        block[d] += 1

ans = []
for i in range(N):
    ans.append(size(i) - len(friends[i]) - block[i] - 1)
print(*ans)

import sys
input = sys.stdin.readline

def find(x):
    # xの根を求める
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x, y):
    # xとyが属する集合を併合する
    x, y = find(x), find(y)
    if x == y:
        return 0
    sx = size(x)
    sy = size(y)
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return sx * sy

def size(x):
    # xが属する集合の要素数を返す
    return -par[find(x)]

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
par = [-1] * N
conv = (N-1) * N // 2
ans = []
for a, b in reversed(AB):
    ans.append(conv)
    conv -= union(a-1, b-1)
    
print(*ans[::-1], sep='\n')

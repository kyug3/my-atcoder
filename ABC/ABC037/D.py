import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

H, W = li()
A = [li() for _ in range(H)]

seen = [[0] * W for _ in range(H)]
def f(h, w, dist, tmp):
    c = 1
    if seen[h][w]:
        return seen[h][w]
    tmp.add((h,w))
    for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        dh = h+i
        dw = w+j
        if (dh,dw) in tmp:
            continue
        if (0 <= dh < H) and (0 <= dw < W) and (A[dh][dw] > A[h][w]):
            c += f(dh, dw, dist+1, tmp)
            c %= mod
    seen[h][w] = c
    tmp.discard((h,w))
    return c
for h in range(H):
    for w in range(W):
        if not seen[h][w]:
            f(h, w, 0, set())

ans = 0
for h in range(H):
    for w in range(W):
        ans += seen[h][w]
        ans %= mod
print(ans)
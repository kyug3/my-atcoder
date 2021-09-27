import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, M = li()
F = [int(input()) for _ in range(N)]
lst = [0] * N

l = 0
r = 0
cnt = [0] * (M+1)
ok = 1
while l < N:
    while r < N:
        if ok:
            cnt[F[r]] += 1
            if cnt[F[r]] > 1:
                ok = 0
            r += 1
        else:
            break
    cnt[F[l]] -= 1
    if ok:
        lst[l] = r
    else:
        lst[l] = r - 1
    if cnt[F[l]] == 1:
        ok = 1
    l += 1
lst[-1] = N

data = [0] * (2*N+1)

def update(l, r, v):
    # 区間[l, r) に vを足す
    L = l + N
    R = r + N
    while L < R:
        if R % 2 == 1:
            data[R-1] += v
            data[R-1] %= mod
            r -= 1
        if L % 2 == 1:
            data[L] += v
            data[L] %= mod
            L += 1
        L //= 2; R //= 2

def query(x):
    # x の総和を求める
    idx = x + N
    ans = data[idx] % mod
    while True:
        idx //= 2
        if idx == 0:
            break
        ans += data[idx]
        ans %= mod
    return ans

update(0, 1, 1)
for i in range(N):
    update(i+1, lst[i]+1, query(i))

print(query(N) - 1)
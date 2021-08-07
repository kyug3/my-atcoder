import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
#mod = 10**9 + 7
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
data = [0] * (2*N+1)
data[N+1] = 1
LR = [li() for _ in range(K)]
LR.sort()

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

for i in range(1, N):
    for l, r in LR:
        if i + l <= N:
            update(i+l, min(N+1, i+r+1), query(i))

print(query(N))
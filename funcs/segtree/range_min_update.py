#https://atcoder.jp/contests/joi2019yo/submissions/26660974

import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))


def update(l, r, v):
    # 区間[l, r)についてvの方が小さければvに更新
    L = l + N
    R = r + N
    while L < R:
        if R % 2 == 1:
            if data[R-1] > v:
                data[R-1] = v
            r -= 1
        if L % 2 == 1:
            if data[L] > v:
                data[L] = v
            L += 1
        L //= 2; R //= 2

def query(x):
    # xの値を取得
    idx = x + N
    ans = data[idx]
    while True:
        idx //= 2
        if idx == 0:
            break
        ans = min(data[idx], ans)
    return ans

N, M = li()
A = li()
data = [10**9] * (2*N + 1)
LR = [li() for _ in range(M)]
for l, r in LR:
    update(l-1, r, l-1)

dp = [0] * (N+1)
for i in range(N):
    L = query(i)
    if L == 10 ** 9:
        dp[i+1] = dp[i] + A[i]
    else:
        dp[i+1] = max(dp[i], A[i] + dp[L])

print(dp[-1])

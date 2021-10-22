import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
A = li()
F = li()
A.sort()
F.sort(reverse=True)

def is_ok(mid):
    cnt = 0
    for i in range(N):
        # x * F[i] <= mid
        x = mid // F[i]
        y = max(A[i] - x, 0)
        cnt += y
    if cnt > K:
        return 0
    else:
        return 1

def binary_search():
    ng = -1
    ok = 10 ** 12 + 5
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search())


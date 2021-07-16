import sys, math
#sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))


N, K = li()
A = li()

def is_ok(idx):
    cnt = 0
    for a in A:
        a -= 1
        cnt += a // idx
    if cnt > K:
        return False
    else:
        return True

def binary_search():
    ng = -1
    ok = 10**9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid == 0:
            return 1
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = binary_search()
print(ans)
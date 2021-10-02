import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
WP = [li() for _ in range(N)]
# 濃度% = 食塩の重さg / 食塩水の重さg

def is_ok(x):
    L = []
    for i in range(N):
        w, p = WP[i]
        L.append((w * (p - x)))
    L.sort(reverse=True)
    if sum(L[:K]) >= 0:
        return True
    else:
        return False

l = 101
r = -1
for _ in range(1000):
    mid = (l + r) / 2
    tf = is_ok(mid)
    if tf:
        r = mid
    else:
        l = mid

print(r)

import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, D, A = li()

XH = [li() for _ in range(N)]
XH.sort(key=lambda x: x[0])

def is_ok(idx, key):
    if XH[idx][0] > key:
        return True
    else:
        return False

def binary_search(key):
    ng = -1
    ok = len(XH)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, key):
            ok = mid
        else:
            ng = mid
    return ok

dam = [0] * (N+1)
ans = 0
total = 0
for i in range(N):
    total += dam[i]
    rest_HP = XH[i][1] - A * total
    if rest_HP <= 0:
        continue
    
    left = XH[i][0]
    right = left + D + D
    count = -(-rest_HP // A)
    ans += count
    total += count

    x = binary_search(right)
    dam[x] -= count
print(ans)

import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())


N, A, B = n_inp()
H = [int(input()) for _ in range(N)]
H.sort(reverse=True)

def is_ok(idx, key, lst=H):
    count = 0
    for h in lst:
        h -= B * idx
        if h > 0:
            x = A - B
            count += (h + (x - 1)) // x
    if count <= idx:
        return True
    else:
        return False

def binary_search(key, lst=H):
    ng = -1
    ok = 10**9+1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, key):
            ok = mid
        else:
            ng = mid
    return ok

ans = binary_search(10**9+1)
print(ans)
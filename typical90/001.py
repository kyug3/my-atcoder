import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

def is_ok(idx, key):
    count = 0
    now = 0
    for i in range(1, N+2):
        length = lst[i] - lst[i-1]
        now += length
        if now >= idx:
            now = 0
            count += 1
    if count > key:
        return False
    else:
        return True

def binary_search(key):
    ng = -1
    ok = L + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, key):
            ok = mid
        else:
            ng = mid
    return ok

N, L = li()
K = int(input())
lst = [0] + li() + [L]
print(binary_search(K) - 1)
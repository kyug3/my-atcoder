import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = [int(input()) for _ in range(N)]
sumA = sum(A)
A = A + A

def is_ok(num):
    l = r = 0
    cnt = 0
    lst = [-2] * (2 * N)
    while l < 2 * N:
        while r < 2 * N:
            if cnt < num:
                cnt += A[r]
                r += 1
            else:
                lst[l] = r
                break
        cnt -= A[l]
        l += 1

    for i in range(N):
        j = lst[i]
        k = lst[j]
        l = lst[k]
        if k >= 0 and j >= 0 and l >= 0 and l - i <= N:
            return False

    return True

ok = sumA + 1
ng = -1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ng)
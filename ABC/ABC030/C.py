import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
import bisect

N, M = li()
X, Y = li()
A = li()
B = li()

idx = A[0] + X
cnt = 1
while 1:
    if cnt % 2:
        i = bisect.bisect_left(B, idx)
        if i == M:
            break
        idx = B[i] + Y
        cnt += 1
    else:
        i = bisect.bisect_left(A, idx)
        if i == N:
            break
        idx = A[i] + X
        cnt += 1

print(cnt // 2)
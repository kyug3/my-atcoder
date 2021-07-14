import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, P, Q = li()
A = li()
ans = 0
for i in range(N-4):
    a = A[i] % P
    for j in range(i+1, N-3):
        b = a * A[j] % P
        for k in range(j+1, N-2):
            c = b * A[k] % P
            for l in range(k+1, N-1):
                d = c * A[l] % P
                for m in range(l+1, N):
                    e = d * A[m] % P
                    if e % P == Q:
                        ans += 1
print(ans)
import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = li()
ruiseki = [0]
for i in range(N):
    ruiseki.append(ruiseki[-1] + A[i])
INF = float('Inf')
memo = [[0] * N for _ in range(N)]
def f(l=0, r=N-1):
    n = r - l + 1
    if n == 1:
        return 0
    if n == 2:
        return A[l] + A[r]
    if memo[l][r]:
        return memo[l][r]
    ans = INF
    for i in range(l, r):
        ans = min(ans, f(l, i) + f(i+1, r))
    ans = ans + ruiseki[r+1] - ruiseki[l]
    memo[l][r] = ans
    return ans
print(f())
import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, K = li()
A = li()
B = li()

diff = 0
for i in range(N):
    diff += abs(A[i] - B[i])

ans = 'No'
if K >= diff and (K-diff) % 2 == 0:
    ans = 'Yes'
print(ans)
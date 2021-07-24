import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = li()
cnt = 0
ans = 0
for i in range(1, N):
    if A[i-1] < A[i]:
        cnt += 1
    else:
        cnt = 0
    ans += cnt
print(ans + N)
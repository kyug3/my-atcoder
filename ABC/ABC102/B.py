import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = li()
ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans = max(ans, abs(A[i] - A[j]))
print(ans)
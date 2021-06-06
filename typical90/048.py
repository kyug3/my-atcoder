import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, K = li()
A = []
for _ in range(N):
    a, b = li()
    A.append(a - b)
    A.append(b)
A.sort(reverse=True)
print(sum(A[:K]))
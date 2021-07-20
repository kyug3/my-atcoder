import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = li()
    A.append(a)
    B.append(b)
A.sort()
B.sort()

if N % 2:
    print(B[N//2] - A[N//2] + 1)
else:
    x = (A[N//2] + A[N//2 - 1]) / 2
    y = (B[N//2] + B[N//2 - 1]) / 2
    print(int(y - x + 1 + y - x))
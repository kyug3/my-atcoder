import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = []
for i in range(N):
    A.append((int(input()), i))
A.sort()

B = [0] * N
now = 0
for i in range(1, N):
    a, idx = A[i]
    if a > A[i-1][0]:
        now += 1
    B[idx] = now
for b in B:
    print(b)

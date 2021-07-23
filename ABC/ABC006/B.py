import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))


mod = 10007
N = int(input())
A = [0] * (N+1)
if N < 3:
    print(0)
    exit()
A[3] = 1
for i in range(4, N+1):
    A[i] += A[i-1] + A[i-2] + A[i-3]  
    A[i] %= mod
print(A[-1])
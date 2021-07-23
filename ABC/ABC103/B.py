import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

S = list(input())
T = list(input())
N = len(T)

for i in range(N):
    U = T[i:] + T[:i]
    if U == S:
        print('Yes')
        exit()
print('No')
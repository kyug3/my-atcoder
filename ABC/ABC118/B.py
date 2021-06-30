import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M = li()
s = set(i for i in range(1, M+1))
for i in range(N):
    ka = li()
    s &= set(ka[1:])
print(len(s))
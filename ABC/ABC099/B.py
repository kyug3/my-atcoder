import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

a, b = li()
dif = abs(a-b)
tot = 0
for i in range(dif):
    tot += i
print(tot - a)
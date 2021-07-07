import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = input().rstrip()
fx = 0
for n in N:
    fx += int(n)
N = int(N)
if N % fx == 0:
    print('Yes')
else:
    print('No')
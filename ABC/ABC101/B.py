import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = input()

sn = 0
for n in N:
    sn += int(n)

N = int(N)
if N % sn == 0:
    print('Yes')
else:
    print('No')
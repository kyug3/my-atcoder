import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
L = li()
L.sort(reverse=True)
if L[0] < sum(L[1:]):
    print('Yes')
else:
    print('No')
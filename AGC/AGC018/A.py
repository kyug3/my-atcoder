import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from functools import reduce


def gcd(nums) -> int:
    return reduce(math.gcd, nums)
N, K = li()
A = li()
m = max(A)
g = gcd(A)
if K % g == 0 and K <= m:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
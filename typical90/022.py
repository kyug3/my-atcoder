import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from functools import reduce


def gcd(nums) -> int:
    return reduce(math.gcd, nums)

A = li()

x = gcd(A)
ans = 0
for i in A:
    ans += i // x - 1
print(ans)
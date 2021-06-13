import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
A = li()

def get_divisors(x: int) -> list:
    divisors = []
    for i in range(1, x):
        if i * i > x:
            break
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)
    divisors = set(divisors)
    divisors.discard(1)
    return divisors

d = set()
for a in A[::-1]:
    x = get_divisors(a)
    if not x.isdisjoint(d):
        break
    d |= x
else:
    print('pairwise coprime')
    exit()

from functools import reduce

def gcd(nums) -> int:
    return reduce(math.gcd, nums)

if gcd(A) != 1:
    print('not coprime')
else:
    print('setwise coprime')
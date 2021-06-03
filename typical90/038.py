import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
import math

A, B = li()
g = math.gcd(A, B)
ans = A*B // g
if ans > 10 ** 18:
    ans = 'Large'
print(ans)
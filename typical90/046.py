import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import defaultdict

N = int(input())
A = li()
B = li()
C = li()

adic = defaultdict(int)
for a in A:
    adic[a % 46] += 1

bdic = defaultdict(int)
for a in B:
    bdic[a % 46] += 1

cdic = defaultdict(int)
for a in C:
    cdic[a % 46] += 1


ans = 0
for ai, av in adic.items():
    for bi, bv in bdic.items():
        for ci, cv in cdic.items():
            if (ai + bi + ci) % 46 == 0:
                ans += av * bv * cv
print(ans)
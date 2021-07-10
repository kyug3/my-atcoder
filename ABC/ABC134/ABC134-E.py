import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from bisect import bisect_left

N = int(input())
lst = [-1] * N
for _ in range(N):
    a = int(input())
    i = bisect_left(lst, a)
    lst[i-1] = a
print(len(lst) - lst.count(-1))
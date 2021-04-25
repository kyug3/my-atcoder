import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())
import heapq
from itertools import combinations
from decimal import *
N, A, B = n_inp()
V = l_inp()

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

ma = 0
count = 0
for i in  range(A, B+1):
    h = V[:i]
    avg = Decimal(sum(h)) / Decimal(i)
    mi = min(h)
    notmi = i - h.count(mi)
    c = i
    heapq.heapify(h)
    for j in range(i, N):
        if V[j] == mi:
            c += 1
        elif V[j] > mi:
            heapq.heappushpop(h, V[j])
            avg = Decimal(sum(h)) / Decimal(i)
            if min(h) == mi:
                notmi += 1
                c += 1
            else:
                mi = min(h)
                notmi = i - h.count(mi)
                c = i
    if ma < avg:
        ma = avg
        count = cmb(c-notmi, h.count(mi))
    elif ma == avg:
        count += cmb(c-notmi, h.count(mi))

            
print(ma)
print(count)

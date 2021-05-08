import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M = li()
ab = [li() for _ in range(M)]
ab.sort(reverse=True)
bridges = [-1]
for i, j in ab:
    if i <= bridges[-1] < j:
        continue
    else:
        bridges.append(i)

print(len(bridges) - 1)
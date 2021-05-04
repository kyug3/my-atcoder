import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M = li()
A = [li() for _ in range(N)]

ans = 0
for i in range(2**3):
    B = sorted(A,
               reverse=True,
               key=lambda x: ((x[0] if (i >> 0) & 1 else -x[0])
                                + (x[1] if (i >> 1) & 1 else -x[1])
                                + (x[2] if (i >> 2) & 1 else -x[2])))
    count = 0
    for l in B[:M]:
        for j in range(3):
            if (i >> j) & 1:
                count += l[j]
            else:
                count -= l[j]
    ans = max(ans, count)
  
print(ans)
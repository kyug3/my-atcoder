import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
import bisect


N = int(input())
A = li()
A.sort()
for _ in range(int(input())):
    B = int(input())
    x = bisect.bisect_left(A, B)
    ans = float('inf')
    for i in range(max(0, x-2), min(N, x+2)):
        ans = min(ans, abs(B - A[i]))
    print(ans)
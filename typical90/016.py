import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
A, B, C = li()

ans = float('inf')
for i in range(10000):
    for j in range(10000-i):
        rest = N - (A*i + B*j)
        if rest < 0:
            break
        if rest % C == 0:
            k = rest // C
            ans = min(ans, i+j+k)
print(ans)
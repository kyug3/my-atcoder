from collections import defaultdict
import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
T, A = li()
def culc(x):
    return T - x * 0.006

best = 10**9
ans = 0
H = li()
for i, h in enumerate(H):
    tmp = culc(h)
    if best > abs(A - tmp):
        best = abs(A-tmp)
        ans = i+1
print(ans)

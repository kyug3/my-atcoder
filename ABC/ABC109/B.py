import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
W = input()
ans = 'Yes'
used = set([W])
for _ in range(N-1):
    nw = input()
    if (W[-1] != nw[0]) or (nw in used):
        ans = 'No'
    used.add(nw)
    W = nw
print(ans)
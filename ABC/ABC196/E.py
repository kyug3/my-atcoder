import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N = int(input())
AT = [li() for _ in range(N)]
Q = int(input())
Xs = li()

L = R = 0
mi, ma = -INF, INF
shift = 0
lst = None
for i in range(N):
    a, t = AT[i]
    if t == 1:
        shift -= a
    elif t == 2:
        L = a + shift
        mi = max(L, mi)
        if not lst and mi >= ma:
            lst = [ma-1, ma]
        if lst:
            ma = mi
    else:
        R = a + shift
        ma = min(ma, R)
        if not lst and mi >= ma:
            lst = [mi, mi+1]
        if lst:
            mi = ma
if not lst:
    lst = [mi, ma]
    
for x in Xs:
    if lst[0] < x < lst[1]:
        print(x - shift)
    elif x <= lst[0]:
        print(mi - shift)
    else:
        print(ma - shift)
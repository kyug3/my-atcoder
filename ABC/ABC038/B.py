import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


h1, w1 = li()
h2, w2 = li()
ans = 'NO'
if h1 == h2 or h1 == w2:
    ans = 'YES'
if w1 == h2 or w1 == w2:
    ans = 'YES'
print(ans)
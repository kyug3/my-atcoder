import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, C, K = li()
# C人乗せられる, K経過するまでに乗せる
mi = 0
ans = 0
count = 0
t = [int(input()) for _ in range(N)]
t.sort()
for T in t:
    if not mi:
        mi = T
    if T > mi+K:
        ans += 1
        count = 0
        mi = T
    count += 1
    if count == C:
        ans += 1
        count = 0
        mi = 0
if count:
    ans += 1
    
print(ans)
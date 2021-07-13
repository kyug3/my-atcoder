import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
lst = []
se = set()
for i in range(min(K, 10**5+1)):
    sN = str(N)
    y = 0
    for s in sN:
        y += int(s)
    N = (N + y) % 10**5
    if N in se:
        cnt = i + 1
        start = N
        break
    lst.append(N)
    se.add(N)
if len(lst) == K:
    print(lst[-1])
    exit()

idx = lst.index(start)
K -= (idx + 1)
lst = lst[idx:]
K %= len(lst)
print(lst[K])


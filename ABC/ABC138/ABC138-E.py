import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
import bisect

s = input()
t = input()
ls = len(s)
lt  =len(t)
aid = ord('a')

idxs = [[] for _ in range(27)]
for i in range(ls):
    idxs[ord(s[i]) - aid].append(i)

cnt = 0
idx = 0
for x in t:
    lst = idxs[ord(x) - aid]
    if not lst:
        print(-1)
        exit()
    ok = -1
    ng = len(lst)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if lst[mid] < idx:
            ok = mid
        else:
            ng = mid
    if ng == len(lst):
        cnt += 1
        idx = lst[0] + 1
    else:
        idx = lst[ng] + 1
    
print(cnt * ls + idx)
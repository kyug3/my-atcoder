import sys, math
#sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import defaultdict

H, W = li()
P = [li() for _ in range(H)]
ans = 0
for i in range(2 << H):
    flag = True
    lst = [1] * W
    cnt = 0
    for j in range(H):
        if (i >> j) & 1:
            cnt += 1
            if flag:
                start = j
                flag = False
            for k in range(W):
                if P[start][k] != P[j][k]:
                    lst[k] = 0
    dic = defaultdict(int)
    if not cnt >= 1:
        continue
    for j in range(W):
        if lst[j]:
            dic[P[start][j]] += 1
    for v in dic.values():
        ans = max(ans, v * cnt)
                        
print(max(1, ans))
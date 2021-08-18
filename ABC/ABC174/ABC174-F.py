import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import defaultdict

N, Q = li()
C = li()
LR = [li() for _ in range(Q)]
LR = [(l-1, r-1) for l, r in LR]
lr_idx = {i: e for e, i in enumerate(LR)}
r_lst = [[] for _ in range(N)]
for i in range(Q):
    l, r = LR[i]
    r_lst[r].append(l)

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        # i番目の要素までの総和を返す
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        # i番目の要素にxを足す
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

bit = BIT(N)
c_dic = {}
ret = {}
for i in range(N):
    c = C[i]
    if c in c_dic:
        bit.add(c_dic[c]+1, -1)
        bit.add(i+1, 1)
        c_dic[c] = i
    else:
        c_dic[c] = i
        bit.add(i+1, 1)
    for l in r_lst[i]:
        ret[(l, i)] = bit.sum(i+1) - bit.sum(l)

for l, r in LR:
    print(ret[(l, r)])


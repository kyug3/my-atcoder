import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
中央値がある値以上をとりうるかの二分探索を考える
中央値がX以上となる区間がそうでない区間の半数以上を占めるかで判定できる

Aを、要素がX以上かどうかで+1と-1の配列に置き換え、区間和がプラスになるなら
その区間の中央値がX以上といえる

累積和を取っておくと、acc[j]>=acc[i]で判定できるので、転倒数に帰着できる
"""

class BIT:
    # 1-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        # i番目の要素までの総和を返す
        # [1, i]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        # [l, r]の総和を返す
        if l == 1:
            return self.sum(r)
        else:
            return self.sum(r) - self.sum(l-1)
  
    def add(self, i, x):
        # i番目の要素にxを足す
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def lower_bound(self, w):
        # 累積和が w 以上となる最小のx
        if w <= 0:
            return 0
        x, r = 0, 1
        while r < self.size:
            r = r << 1
        len = r
        while len > 0:
            if (x + len < self.size and self.tree[x+len] < w):
                w -= self.tree[x + len]
                x += len
            len = len >> 1
        return x + 1


N = int(input())
M = (N + 1) * N // 2
A = li()

def f(X):
    bit = BIT(2*N + 1)
    AA = [-1 if a < X else 1 for a in A]
    acc = [0]
    for a in AA:
        acc.append(acc[-1] + a)
    
    cnt = 0
    for a in acc:
        cnt += bit.sum(N+1+a)
        bit.add(N+1+a, 1)
    return cnt >= M // 2 + M % 2


ok = 10 ** 9 + 1
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ng = mid
    else:
        ok = mid

print(ng)

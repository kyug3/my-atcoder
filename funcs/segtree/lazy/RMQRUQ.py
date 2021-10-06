import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
#mod = 10**9 + 7
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

class LazySegTree:
    # RMQ and RUQ
    # 参考
    # https://smijake3.hatenablog.com/entry/2018/11/03/100133
    def __init__(self, N):
        self.size = 2 ** (N-1).bit_length()
        self.data = [2**31-1] * (2*self.size+1)
        self.lazy = [2**31-1] * (2*self.size+1)
        
    def gindex(self, l, r):
        # 伝搬される区間のインデックス(1-indexed)を全て列挙するgenerator
        L = l + self.size; R = r + self.size
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1
        
    def propagates(self, *ids):
        # 1-indexedで単調増加のインデックスリストを渡す
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None:
                continue
            self.lazy[2*i-1] = self.data[2*i-1] = self.lazy[2*i] = self.data[2*i] = v
            self.lazy[i-1] = None

    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        # 1. トップダウンにlazyの値を伝搬
        self.propagates(*ids)
    
        # 2. 区間[l, r)のdata, lazyの値を更新
        L = self.size + l; R = self.size + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.data[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.data[L-1] = x
                L += 1
            L >>= 1; R >>= 1

        # 3. 伝搬させた区間について、ボトムアップにdataの値を伝搬する
        for i in ids:
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i])

    def minimum(self, l, r):
        # 1. トップダウンにlazyの値を伝搬
        self.propagates(*self.gindex(l, r))
        L = self.size + l; R = self.size + r

        # 2. 区間[l, r)の最小値を求める
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

N, Q = li()
tree = LazySegTree(10**5 + 5)
for _ in range(Q):
    i = li()
    if i[0] == 0:
        s, t, x = i[1:]
        tree.update(s, t+1, x)
    else:
        s, t = i[1:]
        print(tree.minimum(s, t+1))
import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

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

Q = int(input())
bit = BIT(200000)
for _ in range(Q):
    t, x = li()
    if t == 1:
        bit.add(x, 1)
    else:
        ans = bit.lower_bound(x)
        print(ans)
        bit.add(ans, -1)
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

class RangeUpdate:
    def __init__(self, n):
        self.BIT0 = BIT(n + 1)
        self.BIT1 = BIT(n + 1)

    def add(self, l, r, x):
        # [l, r]にxを加算
        self.BIT0.add(l, -x*(l-1))
        self.BIT0.add(r+1, x*r)
        self.BIT1.add(l, x)
        self.BIT1.add(r+1, -x)

    def sum(self, i):
        return self.BIT0.sum(i) + self.BIT1.sum(i) * i
"""
# 配列Aの転倒数を求める
N = int(input())
A = li()
bit = BIT(max(A))
ans = 0
for i in range(N):
    ans += i - bit.sum(A[i]+1)
    bit.add(A[i]+1, 1)

print(ans)
"""
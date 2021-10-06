class RAQRSQ:
    def __init__(self, N):
        self.size = N
        self.data = [0] * (2*N+1)
        self.datb = [0] * (2*N+1)

    def add(self, a, b, x, k, l, r):
        if a <= l and r <= b:
            self.data[k] ^= x
        elif l < b and a < r:
            self.datb[k] ^= (min(b, r) - max(a, l)) * x
            self.add(a, b, x, k * 2 + 1, l, (l+r) // 2)
            self.add(a, b, x, k * 2 + 2, (l+r) // 2, r)

    def sum(self, a, b, k, l, r):
        if b <= l or r <= a:
            return 0
        elif a <= l and r <= b:
            return self.data[k] * (r - l) ^ self.datb[k]
        else:
            res = (min(b, r) - max(a, l)) * self.data[k]
            res += self.sum(a, b, k * 2 + 1, l, (l+r) // 2)
            res += self.sum(a, b, k * 2 + 2, (l+r) // 2, r)
            return res

# 蟻本の再帰による実装、遅い
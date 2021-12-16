class RSQ:
    def __init__(self, N, is_mod=0):
        self.size = N
        self.tree = [0] * (2*N+1)
        self.is_mod = is_mod
        self.mod = 998244353
        # self.mod = 10**9 + 7
    
    def query(self, l, r):
        # return the sum of range [l, r)
        L = l + self.size
        R = r + self.size
        ans = 0
        while L < R:
            if R % 2 == 1:
                R -= 1
                ans += self.tree[R]
            if L % 2 == 1:
                ans += self.tree[L]
                L += 1
            if self.is_mod:
                ans %= self.mod
            L //= 2; R //= 2
        return ans
    
    def update(self, i, v):
        # add v to A[i]
        idx = i + self.size
        self.tree[idx] += v
        if self.is_mod:
            self.tree[idx] %= self.mod
        while 1:
            idx //= 2
            if idx == 0:
                break
            self.tree[idx] += v
            if self.is_mod:
                self.tree[idx] %= self.mod
    
N, Q = map(int, input().split())
tree = RSQ(N+1)

for _ in range(Q):
    q, x, y = map(int, input().split())
    if q == 0:
        tree.update(x, y)
    else:
        print(tree.query(x, y+1))
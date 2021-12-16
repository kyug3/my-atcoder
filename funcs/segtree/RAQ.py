class RAQ:
    def __init__(self, N, is_mod=0):
        self.size = N
        self.tree = [0] * (2*N+1)
        self.is_mod = is_mod
        self.mod = 998244353
        # self.mod = 10**9 + 7

    def update(self, l, r, v):
        # add v to range [l, r)
        L = l + self.size
        R = r + self.size
        while L < R:
            if R % 2:
                R -= 1
                self.tree[R] += v
                if self.is_mod:
                    self.tree[R] %= self.mod
            if L % 2:
                self.tree[L] += v
                if self.is_mod:
                    self.tree[L] %= self.mod
                L += 1
            L //= 2; R //= 2
    
    def query(self, i):
        # return the value of A[i]
        idx = i + self.size
        ans = self.tree[idx]
        while 1:
            idx //= 2
            if idx == 0:
                break
            ans += self.tree[idx]
            if self.is_mod:
                ans %= self.mod
        return ans

# AOJ DSL_2_E
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_E

N, q = map(int, input().split())
tree = RAQ(N+1)
for _ in range(q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        l, r, v = tmp[1:]
        tree.update(l, r+1, v)
    else:
        print(tree.query(tmp[1]))


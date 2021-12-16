class RUQ:
    def __init__(self, N):
        self.size = N
        self.tree = [(-1, 2**31-1)] * (2*N + 1)

    def update(self, l, r, v):
        # change range [l, r) to v
        # v is tuple
        L = l + self.size
        R = r + self.size
        while L < R:
            if R % 2:
                R -= 1
                self.tree[R] = v
            if L % 2:
                self.tree[L] = v
                L += 1
            L //= 2; R //= 2
    
    def query(self, i):
        # return the value of A[i]
        # data[idx][0]が大きいものほど新しい
        idx = i + self.size
        ans = self.tree[idx]
        while True:
            idx //= 2
            if idx == 0:
                break
            if ans[0] < self.tree[idx][0]:
                ans = self.tree[idx]
        return ans[1]
    

N, Q = map(int, input().split())
tree = RUQ(N+1)

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        l, r, x = q[1:]
        tree.update(l, r+1, (i, x))
    else:
        print(tree.query(q[1]))
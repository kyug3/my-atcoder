class RMU:
    def __init__(self, N):
        # 区間[l, r)についてvの方が大きければvに更新
        self.size = N
        self.inf = -1
        self.tree = [self.inf] * (2*N+1)

    def update(self, l, r, v):
        L = l + self.size
        R = r + self.size
        while L < R:
            if R & 1:
                R -= 1
                self.tree[R] = max(self.tree[R], v)
            if L & 1:
                if self.tree[L] < v:
                    self.tree[L] = max(self.tree[L], v)
                L += 1
            L >>= 1; R >>= 1
    
    def query(self, x):
        # xの値を取得
        idx = x + self.size
        ans = self.tree[idx]
        while 1:
            idx >>= 1
            if idx == 0:
                break
            ans = max(self.tree[idx], ans)
        return ans
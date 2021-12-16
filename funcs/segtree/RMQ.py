# N = 配列の長さ
# self.tree[N] が初期配列の 0 に対応する
class RMQ:
    def __init__(self, N):
        self.size = N
        self.inf = 2**31-1
        self.tree = [self.inf] * (2*N+1)

    def query(self, l, r):
        # return minimum element in range [l, r) 
        L = l + self.size
        R = r + self.size
        ans = self.inf
        while L < R:
            if R % 2:
                R -= 1
                ans = min(ans, self.tree[R])
            if L % 2:
                ans = min(ans, self.tree[L])
                L += 1
            L //= 2; R //= 2
        return ans
    
    def update(self, i, v):
        # change A[i] to v
        idx = i + self.size
        self.tree[idx] = v
        while 1:
            idx //= 2
            if idx == 0:
                break
            a, b = self.tree[idx*2+1], self.tree[idx*2]
            self.tree[idx] = min(a, b)
 

# AOJ DSL_2_A
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_A

N, Q = map(int, input().split())
tree = RMQ(10**5 + 1)

for _ in range(Q):
    q, x, y = list(map(int, input().split()))
    if q == 0:
        tree.update(x, y)
    else:
        print(tree.query(x, y+1))

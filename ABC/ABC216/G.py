import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
Rを昇順にソートして右から埋めていく
必要数-区間合計を取ることでその区間にあと何個必要か求める
R以下でまだ使ってないインデックスを右から取っていく
インデックスを管理する配列に今見てる区間のRまでappendして、
必要数だけpopすることを繰り返せばよい

想定解は牛ゲーらしい
"""

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

N, M = li()
RLX = []
for _ in range(M):
    l, r, x = li()
    l -= 1; r -= 1
    RLX.append((r, l, x))

RLX.sort()

tree = RSQ(N+1)
ans = [0] * N

idx = 0
lst = []
for r, l, x in RLX:
    n = tree.query(l, r+1)

    while r >= idx:
        lst.append(idx)
        idx += 1
    x -= n
    while x > 0:
        use = lst.pop()
        ans[use] = 1
        tree.update(use, 1)
        x -= 1
    
print(*ans)
import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

class RMQ:
    def __init__(self, N):
        self.size = N
        self.inf = 0
        self.tree = [self.inf] * (2*N+1)

    def query(self, l, r):
        # return minimum element in range [l, r) 
        L = l + self.size
        R = r + self.size
        ans = self.inf
        while L < R:
            if R % 2:
                R -= 1
                ans = max(ans, self.tree[R])
            if L % 2:
                ans = max(ans, self.tree[L])
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
            self.tree[idx] = max(a, b)
 
N = int(input())
H = li()
A = li()
tree = RMQ(N+2)
ans = 0
for i in range(N):
    ma = tree.query(0, H[i])
    val = ma + A[i]
    ans = max(ans, val)
    tree.update(H[i], val)

print(ans)
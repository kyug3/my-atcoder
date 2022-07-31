import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
あるロボットだけを動かしたとき、どのロボットまで動くのかを区間を考えると、
共通部分を持たないような区間の選び方のDPとして数えられる。

区間の右端はそのロボットが起動させるロボットの持つ区間の最大値になるので、
右のロボットから見ていくと区間最大のセグメントツリーで区間を取得できる。

起動させるロボットの右端は二分探索する。
"""

class RMQ:
    def __init__(self, N):
        self.size = N
        self.inf = -(2**31-1)
        self.tree = [self.inf] * (2*N+1)

    def query(self, l, r):
        # return max element in range [l, r) 
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
XD = [tuple(li()) for _ in range(N)]
XD.sort()

from bisect import bisect_left
lst = [-(10 ** 10)] * N
tree = RMQ(N + 1)

for i in range(N)[::-1]:
    right = bisect_left(lst, XD[i][0] + XD[i][1])
    left = i
    x = tree.query(left, right)
    tree.update(i, max(i, x))
    lst[i] = XD[i][0]

rng = []
for i in range(N):
    j = tree.query(i, i+1)
    rng.append((i, j))

dp = [0] * (N+1)
dp[0] = 1
for i in range(N):
    dp[i+1] += dp[i]
    dp[i+1] %= mod
    dp[rng[i][1]+1] += dp[i]
    dp[rng[i][1]+1] %= mod

print(dp[-1] % mod)
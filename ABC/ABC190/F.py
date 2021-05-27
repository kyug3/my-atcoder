import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        # i番目の要素までの総和を返す
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        # i番目の要素にxを足す
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N = int(input())
A = li()
bit = BIT(N)
ans = 0
for i in range(N):
    ans += i - bit.sum(A[i]+1)
    bit.add(A[i]+1, 1)

print(ans)

for i in range(N-1):
    ans -= A[i]
    ans += N - 1 - A[i]
    print(ans)
    
    

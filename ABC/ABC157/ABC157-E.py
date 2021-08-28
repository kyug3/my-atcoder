import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

class BIT:
    # 1-indexed
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
    
    def range_sum(self, l, r):
        if l == 1:
            return self.sum(r)
        else:
            return self.sum(r) - self.sum(l-1)
  
    def add(self, i, x):
        # i番目の要素にxを足す
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

dic = {chr(i): e for e, i in enumerate(range(ord('a'), ord('z') + 1))}
N = int(input())
S = list(input())
bits = [BIT(N+5) for _ in range(26)]
for i in range(N):
    bits[dic[S[i]]].add(i+1, 1)

for i in range(int(input())):
    q, i, c = input().split()
    if q == '1':
        i = int(i)
        if S[i-1] == c:
            continue
        bits[dic[S[i-1]]].add(i, -1)
        bits[dic[c]].add(i, 1)
        S[i-1] = c
    else:
        l, r = int(i), int(c)
        ans = 0
        for i in range(26):
            if bits[i].range_sum(l, r):
                ans += 1
        print(ans)
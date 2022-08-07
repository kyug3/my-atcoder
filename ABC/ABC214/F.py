import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
大筋は部分列DP
基本はその文字を使うかどうかの二択だが、重複が出るのが厄介
ある文字列の作り方が複数あるときは、できるだけ左に詰めて選ぶことを考える

dp[i]: i文字目を最後に使った場合の数
dic[s]: 前回出てきたsのindex

i文字目の文字をsとする
i文字目を使って作れる新しい文字は、区間[ dic[s]-1, i-1 )に含まれる文字を使った場合になる
(dic[s]がない場合は左端は0)
(区間については、部分列DPの性質と、隣を使えないという問題条件から分かる)

DPテーブルは|S|+2の長さを持っておき、dp[0]=1, dp[1]=0と初期化しておく
(初期化として絶対に選ばなければいけない文字を先頭に置いておきたいが、
隣を使えない条件があるため、0にそれを置いて、1を挟んでおいて2からスタートするイメージ)
"""

class RSQ:
    def __init__(self, N, is_mod=0):
        self.size = N
        self.tree = [0] * (2*N+1)
        self.is_mod = is_mod
        # self.mod = 998244353
        self.mod = 10**9 + 7
    
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
from collections import defaultdict

S = input()
N = len(S)
dp = RSQ(N+2, 1)
dp.update(0, 1)
dic = defaultdict(lambda: 1)

for i in range(N):
    s = S[i]
    x = dp.query(dic[s]-1, i+1)
    dp.update(i+2, x)
    dic[s] = i+2 

print(dp.query(2, N+2)) 

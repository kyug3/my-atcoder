import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

#https://atcoder.jp/contests/past202203-open/tasks/past202203_n

"""
Ai - Aj が何個書かれたかは指数部にAiと-Ajを取った多項式の積の係数になる。
配列のインデックスが指数部の値に対応するようにしてconvに突っ込むと
係数が0でない項の数が答え
"""

import numpy as np
from numpy.fft import rfft, irfft
 
def conv(aa, bb):
    m = len(aa)+len(bb)
    m = 1 << (m-1).bit_length()
    res = (irfft(rfft(aa, m)*rfft(bb, m))+0.5).astype("i8")
    return res[:len(aa)+len(bb)-1]

N = int(input())
A = li()
a = np.zeros(200000, dtype='i8')
b = np.zeros(200000, dtype='i8')

for i in range(N):
    a[A[i]-1] += 1
    b[200000 - A[i]] += 1

res = conv(a, b)
ans = np.sum(res > 0)
print(ans)
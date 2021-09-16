import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

"""
あるAとB(A > B)について
abs(A - B) = C
abs(B - C) = D
といった操作を繰り返すとユークリッドの互除法のようになり、
最終的にAとBの最大公約数のボール G を入れられることがわかる。
GはAの約数なのでAとGを用いてA以下の全てのGの倍数を入れられる。
"""

N, K = li()
A = li()
maxA = max(A)

gcd = A[0]
for i in range(1, N):
    gcd = math.gcd(gcd, A[i])

if maxA >= K and K % gcd == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
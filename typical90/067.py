import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
if N == 0:
    print(0)
    exit()
N = str(N)
for i in range(K):
    cnt = 0
    for e, s in enumerate(N[::-1]):
        cnt += int(s) * (8 ** e)
    M = ''
    while cnt > 0:
        M += str(cnt % 9)
        cnt //= 9
    N = ''
    for m in M[::-1]:
        if m == '8':
            m = '5'
        N += m
print(N)

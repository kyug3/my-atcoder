import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

H, W = li()
A = [li() for _ in range(H)]
B = [li() for _ in range(H)]

ans = 0
for h in range(H-1):
    for w in range(W-1):
        dif = A[h][w] - B[h][w]
        A[h][w] -= dif
        ans += abs(dif)
        for i, j in ((1, 0), (0, 1), (1, 1)):
            A[h+i][w+j] -= dif

if A != B:
    print('No')
else:
    print('Yes')
    print(ans)
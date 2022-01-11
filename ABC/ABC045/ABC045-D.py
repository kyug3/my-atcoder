import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
from collections import defaultdict

H, W, N = li()

def inside(h, w):
    return 2 <= h < H and 2 <= w < W

dic = defaultdict(int)
for _ in range(N):
    a, b = li()
    for i in range(-1, 2):
        for j in range(-1, 2):
            h, w = a+i, b+j
            if inside(h,w):
                dic[(h, w)] += 1

al = (H-2) * (W-2)
ans = [0] * 10
ans[0] = al
for v in dic.values():
    ans[v] += 1
    ans[0] -= 1

for a in ans:
    print(a)

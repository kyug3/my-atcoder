import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
import bisect

N = int(input())
dic = {'R': 0, 'G': 1, 'B': 2}
RGB = [[] for _ in range(3)]

for _ in range(2*N):
    a, c = input().split()
    a = int(a)
    RGB[dic[c]].append(a)

cnt = 0
for i in range(3):
    if len(RGB[i]) % 2 == 0:
        RGB[0], RGB[i] = RGB[i], RGB[0]
        cnt += 1

for i in range(3):
    RGB[i].sort()

if cnt == 3:
    print(0)
    exit()

ans = INF
for i in range(len(RGB[1])):
    x = RGB[1][i]
    idx = bisect.bisect_left(RGB[2], x)
    for j in range(idx-2, idx+3):
        if 0 <= j < len(RGB[2]):
            ans = min(ans, abs(x - RGB[2][j]))

lst1 = []
lst2 = []

for i in range(len(RGB[0])):
    x = RGB[0][i]
    idx1 = bisect.bisect_left(RGB[1], x)
    tmp1 = INF
    for j in range(idx1 - 2, idx1 + 3):
        if 0 <= j < len(RGB[1]):
            tmp1 = min(tmp1, abs(x - RGB[1][j]))
    lst1.append((tmp1, i))

    idx2 = bisect.bisect_left(RGB[2], x)
    tmp2 = INF
    for j in range(idx2 - 2, idx2 + 3):
        if 0 <= j < len(RGB[2]):
            tmp2 = min(tmp2, abs(x - RGB[2][j]))
    lst2.append((tmp2, i))

lst1.sort()
lst2.sort()
l = len(lst1)
for i in range(min(3, l)):
    a, b = lst1[i]
    for j in range(min(3, l)):
        c, d = lst2[j]
        if b != d:
            ans = min(ans, a + c)
print(ans)
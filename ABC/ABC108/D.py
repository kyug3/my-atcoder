import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
Xのグラフが構築できるとX+1と2Xのグラフも
簡単に構築できるので2進数でやりたくなるね

+1は、スタートからゴールにその値の重みの辺を張る

2Xは、今ある全ての辺の重みを2倍し、
新しいゴールを作り、古いゴールから0と1の辺を張る
"""

L = int(input())
B = bin(L)[2:]
N = len(B)
ans = [[1, 2, 0], [1, 2, 1]]
now = 2
if B[1] == '1':
    now = 3
    ans.append([1, 2, 2])

for i in range(2, N):
    now *= 2
    for j in range(len(ans)):
        ans[j][2] *= 2
    ans.append([i, i+1, 0])
    ans.append(([i, i+1, 1]))
    if B[i] == '1':
        ans.append([1, i+1, now])
        now += 1

print(N, len(ans))
for a in ans:
    print(*a)
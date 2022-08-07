import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
from heapq import *

"""
今見てる箱の番号がiのとき、L<=iのボールを全てヒープに入れ、Rの最小を取り出す
箱の番号を++1し、L<=iのボールを入れRの最小を取り出す

という操作をi=1から順に繰り替えることを考える。

ここで、ヒープが空のとき、箱の数字が小さすぎるので、箱の番号を
まだ見てないボールのうち最小のLに変更する。

取り出した R < iだったり最後までヒープに要素が残ったらNo
そうでなければYes
"""

def f():
    N = int(input())
    LR = [tuple(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: (x[0], [1]))

    hq = []
    box = -1
    idx = 0
    while box <= 10**9:
        if not hq and idx < N:
            l, r = LR[idx]
            box = l
        while idx < N and LR[idx][0] <= box:
            heappush(hq, LR[idx][1])
            idx += 1
        if not hq:
            break
        r = heappop(hq)
        if r < box:
            print('No')
            return
        box += 1
    if hq:
        print('No')
    else:
        print('Yes')
    return


T = int(input())
for _ in range(T):
    f()
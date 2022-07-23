import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


"""
dp[L][R] 区間[L,R)の範囲で勝負したときのgrundy数
区間[L,R)が与えられたとき、その範囲内の区間[l, r)を選択すると、
[L,l)と[r,R)のゲームに分割される。
区間DPの要領で部分ゲームのgrundy数を取っていき、[1,100)のgrundy数で判定。
"""

def f():
    N = int(input())
    M = 100
    LR = [li() for _ in range(N)]
    dp = [[0] * (M+1) for _ in range(M+1)]
    for w in range(M+1):
        for l in range(1, M):
            r = l + w
            if r > M:
                break

            lst = [0] * (N+1)
            for i in range(N):
                if l <= LR[i][0] and LR[i][1] <= r:
                    lst[dp[l][LR[i][0]] ^ dp[LR[i][1]][r]] = 1

            mex = 0
            for i in range(N+1):
                if not lst[i]:
                    mex = i
                    break
            dp[l][r] = mex

    ans = "Bob"
    if dp[1][M]:
        ans = "Alice"
    return ans

T = int(input())
out = []
for _ in range(T):
    out.append(f())

print(*out, sep='\n')
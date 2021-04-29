import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())

N = int(input())
S = [list(input().rstrip()) for _ in range(2)]
if N == 1:
    print(3)
    exit()

if S[0][0] == S[0][1]:
    if N == 2:
        print(6)
        exit()
    start = 2
    ans = 6
else:
    start = 1
    ans = 3
if S[0][-2] == S[0][-1]:
    end = -2
else:
    end = -1

skip = False
for i, j in enumerate(range(start, N+end)):
    s1 = S[0][j]
    s2 = S[1][j]
    i += start
    if skip:
        skip = False
        continue
    if s1 == s2:
        if S[0][i-1] == S[1][i-1]:
            ans *= 2
    else:
        skip = True
        if S[0][i-1] == S[1][i-1]:
            ans *= 2
        else:
            ans *= 3
    ans %= mod
else:
    
    s1 = S[0][end]
    s2 = S[1][end]
    if s1 == s2:
        if S[0][end-1] == S[1][end-1]:
            ans *= 2
        else:
            pass
    else:
        if S[0][end-1] == S[1][end-1]:
            ans *= 2
        else:
            ans *= 3
    ans %= mod

print(ans % mod)

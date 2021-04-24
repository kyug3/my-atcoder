import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def g_inp(N, M):
    g = [[] for _ in range(N)]
    for _ in range(M):
        a, b, z = map(int, input().split())
        a -= 1; b -= 1
        g[a].append((z, b))
        g[b].append((z, a))
    return g
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())

N = int(input())
S = list(input().rstrip())

def func(A: list):
    for i in range(1, len(S)):
        if S[i] == 'o':
            if A[i] == 'S':
                A.append(A[i-1])
            else:
                x = 'S' if A[i-1] == 'W' else 'W'
                A.append(x)
        else:
            if A[i] == 'S':
                x = 'S' if A[i-1] == 'W' else 'W'
                A.append(x)
            else:
                A.append(A[i-1])
    
    if A[0] == 'S':
        if S[0] == 'o':
            tf = True if A[1] == A[N-1] else False
        else:
            tf = True if A[1] != A[N-1] else False
    else:
        if S[0] == 'o':
            tf = True if A[1] != A[N-1] else False
        else:
            tf = True if A[1] == A[N-1] else False
    
    if A[0] != A[-1]:
        tf = False

    return tf, A

for l in (['S', 'S'], ['S', 'W'], ['W', 'S'], ['W', 'W']):
    tf, A = func(l)
    if tf:
        print(''.join(A[:-1]))
        exit()
print(-1)

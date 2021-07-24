import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))


N = int(input())
S = input()

for i in range(N):
    if S[i] == '1':
        if i % 2 == 0:
            print('Takahashi')
        else:
            print('Aoki')
        exit()
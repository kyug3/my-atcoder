import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
grid = [input() for _ in range(N)]
grid = list(zip(*grid[::-1]))
for g in grid:
    print(''.join(g))
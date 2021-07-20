import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, L = li()

kuji = [[''] + list(input()) + [''] for _ in range(L+1)]

for e, s in enumerate(range(1, N*2, 2), 1):
    w = s
    for h in range(L):
        if kuji[h][w+1] == '-':
            w += 2
        elif kuji[h][w-1] == '-':
            w -= 2
    if len(kuji[-1]) > w and (kuji[h+1][w] == 'o'):
        print(e)
        break
        
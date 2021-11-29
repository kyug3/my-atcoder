import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

x = bin(int(input()))
if x == bin(1):
    print('Aoki')
    exit()
N = len(x[2:])
if N % 2 == 1:
    ans = 'Aoki'
    for e, i in enumerate(x[3:]):
        if i == '0' and e % 2 == 0:
            ans = 'Takahashi'
            break
        if i == '1' and e % 2 == 1:
            break
else:
    ans = 'Takahashi'
    for e, i in enumerate(x[3:]):
        if i == '0' and e % 2 == 1:
            ans = 'Aoki'
            break
        if i == '1' and e % 2 == 0:
            break

print(ans)
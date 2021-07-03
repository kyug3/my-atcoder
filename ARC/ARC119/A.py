import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

def f(a, b, c):
    return a * (2 ** b) + c

a = 1
b = 0
c = 0
N = int(input())
for i in range(10**8):
    y = f(a, i, c)
    if y > N:
        b = i-1
        break

ans = float('inf')
for i in range(b+1):
    j = N // (2 ** i)
    k = N % (2 ** i)
    ans = min(ans, i+j+k)
print(ans)

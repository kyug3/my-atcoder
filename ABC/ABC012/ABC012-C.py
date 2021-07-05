import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
x = 2025 - N
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == x:
            print(str(i) + ' x ' + str(j))
import sys, math
from collections import deque
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

H, W = li()
if H == 1 or W == 1:
    print(H*W)
    exit()

print((H+1) // 2 * ((W+1) // 2))
import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())

N = int(input())
S = list(input().rstrip())
ans = deque(S)

count = [0, 0]

for i in range(N):
    if S[i] == ')':
        if count[0] <= count[1]:
            ans.appendleft('(')
            count[0] += 1
        count[1] += 1
    else:
        count[0] += 1
else:
    if count[0] > count[1]:
        for i in range(count[0] - count[1]):
            ans.append(')')
print(''.join(ans))
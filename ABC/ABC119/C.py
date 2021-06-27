import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, A, B, C = li()
ls = [int(input()) for _ in range(N)]

ans = []
def dfs(a, b, c, idx, count):
    if idx >= N:
        if a > 0 and b > 0 and c > 0:
            x = abs(A-a) + abs(B-b) + abs(C-c) + count
            ans.append(x)
    else:
        if a:
            dfs(a+ls[idx], b, c, idx+1, count+10)
        else:
            dfs(a+ls[idx], b, c, idx+1, count)
        if b:
            dfs(a, b+ls[idx], c, idx+1, count+10)
        else:
            dfs(a, b+ls[idx], c, idx+1, count)
        if c:
            dfs(a, b, c+ls[idx], idx+1, count+10)
        else:
            dfs(a, b, c+ls[idx], idx+1, count)
        dfs(a, b, c, idx+1, count)

dfs(0,0,0,0,0)
print(min(ans))

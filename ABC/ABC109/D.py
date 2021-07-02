import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

H, W = li()
A = [li() for _ in range(H)]
ans = []
flag = False
for h in range(H):
    flag = False
    for w in range(W-1):
        if A[h][w] % 2:
            if flag:
                flag = False
            else:
                flag = True
                ans.append((h+1, w+1, h+1, w+2))
        else:
            if flag:
                ans.append((h+1, w+1, h+1, w+2))
    else:
        if flag:         
            A[h][-1] += 1

flag = False
for h in range(H-1):
    if A[h][-1] % 2:
        if flag:
            flag = False
        else:
            flag = True
            ans.append((h+1, W, h+2, W))
    else:
        if flag:
            ans.append((h+1, W, h+2, W))


print(len(ans))
for x in ans:
    print(*x)
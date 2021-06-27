import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))


A, B = li()
if A == B:
    print(A)
    exit()

if A % 2 == 0:
    if B % 2 == 1:
        ans = (1+B-A) // 2 % 2 
    else:
        ans = (1+(B-1)-A) // 2 % 2 ^ B
else:
    if B % 2 == 1:
        ans = (1+(B)-(A+1)) //2 % 2 ^ A
    else:
        ans = (1+(B-1)-(A+1)) // 2 % 2 ^ A ^ B
print(ans)

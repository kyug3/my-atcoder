import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
A = li()
ans = N
xor = A[0]
su = A[0]
left = 0
right = 1
seen = [0] * (N+1)
while right < N:
    if left >= right:
        right += 1
    elif left < right:
        if not seen[right]:
            xor ^= A[right]
            su += A[right]
            seen[right] = 1
        if xor == su:
            ans += right - left
            if right < N:
                right += 1
        else:
            xor ^= A[left]
            su -= A[left]
            left += 1

print(ans)
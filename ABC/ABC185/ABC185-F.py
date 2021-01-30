import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [None] * (N+1) + list(map(int, input().split()))

for i in range(1, N+1)[::-1]:
    if len(A) == i * 2 + 1:
        A[i] = A[i*2]
    else:
        A[i] = A[i*2] ^ A[i*2 + 1]

def xor(x, y):
    idx = x + N
    A[idx] ^= y
    while True:
        idx //= 2
        if idx == 0:
            break
        A[idx] ^= y

def out(l, r):
    l += N
    r += N
    ans = 0
    while l < r:
        if l % 2 == 1:
            ans ^= A[l]
            l += 1
        l //= 2
        if r % 2 == 1:
            ans ^= A[r-1]
            r -= 1
        r //= 2
    return ans


for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        xor(x, y)
    else:
        print(out(x, y+1))

from collections import deque

N = int(input())
A = list(map(int, input().split()))
b = deque([])

side = 0
for i in range(N):
    if i % 2 == 0:
        b.appendleft(A[i])
    else:
        b.append(A[i])

b = list(b)
if len(b) % 2 == 0:
    b = b[::-1]

print(*b)

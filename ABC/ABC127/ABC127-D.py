import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = []
for _ in range(M):
    BC.append(list(map(int, input().split())))
    
BC.sort(reverse=True, key=lambda x: x[1])
count = 0
for m in range(M):
    B, C = BC[m]
    count += B
    if count >= N:
        B -= count - N
    for b in range(B):
        A.append(C)
    if count >= N:
        break

A.sort(reverse=True)
print(sum(A[:N]))
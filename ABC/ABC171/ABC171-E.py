N = int(input())
A = list(map(int, input().split()))

s = A[0]
for a in A[1:]:
    s ^= a

ans = []
for a in A:
    ans.append(s ^ a)

print(*ans)
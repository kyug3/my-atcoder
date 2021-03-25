N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
size = 0
for i in range(N-1):
    size += A[i]
    if size * 2 >= A[i+1]:
        ans += 1
    else:
        ans = 0

print(ans + 1)

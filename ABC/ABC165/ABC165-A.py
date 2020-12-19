K = int(input())
A, B = map(int, input().split())
ans = 'NG'
for x in range(A, B + 1):
    if x % K == 0:
        ans = 'OK'
print(ans)
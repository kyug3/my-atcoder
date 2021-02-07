N = int(input())
P = list(map(int, input().split()))

ans = 0
skip = False
for i in range(N):
    if skip:
        skip = False
        continue
    if P[i] == i+1:
        skip = True
        ans += 1
print(ans)
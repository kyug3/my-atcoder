N = int(input())
A = list(map(int, input().split()))

bucket = [0] * (10**5 + 1)
for a in A:
    bucket[a] += 1

for i in range(len(bucket)):
    if bucket[i] >= 3:
        if bucket[i] % 2:
            bucket[i] = 1
        else:
            bucket[i] = 2

ans = sum(1 for i in bucket if i >= 1)
if bucket.count(2) % 2:
    ans -= 1
print(ans)
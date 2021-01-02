N = int(input())
A = sorted(map(int, input().split()))
MAX = 10 ** 6 + 1
count = [0] * MAX
for a in A:
    count[a] += 1

seen = [0] * MAX
ans = 0
for a in A:
    if seen[a]:
        continue
    for i in range(a, MAX, a):
        seen[i] = 1
    if count[a] == 1:
        ans += 1
print(ans)
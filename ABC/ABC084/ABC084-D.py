import sys
input = sys.stdin.readline

Q = int(input())
MAX = 10 ** 5 + 1
prime = [1 for _ in range(MAX)]
prime[0], prime[1] = 0, 0
for i in range(2, MAX):
    if not prime[i]:
        continue
    for j in range(i * 2, MAX, i):
        prime[j] = 0

a = [0 for _ in range(MAX)]
for i in range(3, MAX, 2):
    if prime[i] and prime[(i + 1) // 2]:
        a[i] = 1
s = []
count = 0
for i in range(MAX):
    count += a[i]
    s.append(count)

for _ in range(Q):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])

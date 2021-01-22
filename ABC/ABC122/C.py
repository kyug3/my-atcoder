N, Q = map(int, input().split())
S = input()

c = [0] # 0からiまでのACの個数
last = S[0]
count = 0
for i in range(1, N):
    now = S[i]
    if last == 'A' and now == 'C':
        count += 1
    c.append(count)
    last = now

for _ in range(Q):
    l, r = map(int, input().split())
    print(c[r-1] - c[l-1])
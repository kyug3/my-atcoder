N = int(input())
A = [int(input()) for _ in range(N)]

seen = [0] * N

x = A[0] - 1
count = 1
while True:
    if seen[x]:
        print(-1)
        break
    if x == 1:
        print(count)
        break
    count += 1
    seen[x] = 1
    x = A[x] - 1
    
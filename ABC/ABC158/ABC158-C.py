A, B = map(int, input().split())
n = 1
while True:
    if n * 8 // 100 == A and n * 10 // 100 == B:
        print(n)
        break
    if n * 8 // 100 > A and n * 10 // 100 > B:
        print(-1)
        break
    n += 1

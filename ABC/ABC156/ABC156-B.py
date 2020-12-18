N, K = map(int, input().split())
n = 1
while True:
    if K ** n > N:
        print(n)
        break
    n += 1

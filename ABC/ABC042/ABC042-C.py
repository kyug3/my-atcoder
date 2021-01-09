N, K = map(int, input().split())
D = set(input())

for i in range(N, 10 ** 7):
    for s in str(i):
        if s in D:
            break
    else:
        print(int(i))
        exit()
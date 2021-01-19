N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
ssum = sum(S)
if ssum % 10 != 0:
    print(ssum)
    exit()
for s in S:
    if s % 10 != 0:
        print(ssum - s)
        break
else:
    print(0)
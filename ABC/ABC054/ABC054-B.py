N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        if [x[i: i+M] for x in A[j: j+M]] == B:
            print('Yes')
            exit()
print('No')

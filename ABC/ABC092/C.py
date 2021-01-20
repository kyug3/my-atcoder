N = int(input())
A = [0] + list(map(int, input().split())) + [0]
a1 = [0]
a2 = [0]
N += 2
for i in range(1, N):
    a1.append(a1[-1] + abs(A[i] - A[i-1]))
    a2.append(a2[-1] + abs(A[N-i-1] - A[N-i]))

for i in range(1, N - 1):
    cut = abs(A[i-1] - A[i+1])
    print(a1[i-1] + a2[N-2-i] + cut)

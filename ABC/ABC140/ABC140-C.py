import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))
A = []
A.append(B[0])
A.append(B[0])
for n in range(1, N - 1):
    x = A.pop()
    A.append(min(B[n], x))
    A.append(B[n])
print(sum(A))
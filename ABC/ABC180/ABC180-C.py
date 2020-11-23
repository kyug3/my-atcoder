import sys
input = sys.stdin.readline

N = int(input())
lst = []
for n in range(1, N+1):
    if n ** 2 == N:
        lst.append(n)
    if n ** 2 >= N:
        break
    if N % n == 0:
        lst.append(n)
        lst.append(N // n)
lst.sort()
for l in lst:
    print(l)
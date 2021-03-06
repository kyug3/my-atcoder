from collections import defaultdict

mod = 10 ** 9 + 7
N = int(input())
T = defaultdict(int)
for _ in range(N):
    T[int(input())] += 1

T = sorted(T.items())
time = 0
su = 0
for k, v in T:
    for i in range(v):
        su += k
        time += su

com = 1
for k, v in T:
    su = 1
    for i in range(v):
        su *= (i+1)
        su %= mod
    com *= su
    com %= mod

print(time)
print(com)

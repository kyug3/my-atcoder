import sys
input = sys.stdin.readline

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

AB = []
for a in A:
    for b in B:
        AB.append(a+b)

AB = sorted(AB, reverse=True)[:K]
ans = []
for a in AB:
    for c in C:
        ans.append(a + c)
ans.sort(reverse=True)

for a in ans[:K]:
    print(a)
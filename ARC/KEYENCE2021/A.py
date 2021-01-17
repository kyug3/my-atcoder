N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_max = 0
c_max = 0
C = []
for a, b in zip(A, B):
    a_max = max(a_max, a)
    c_max = max(c_max, a_max * b)
    C.append(c_max)

for c in C:
    print(c)
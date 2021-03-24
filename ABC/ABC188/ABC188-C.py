N = int(input())
A = list(map(int, input().split()))
len_a = len(A)

max_A_l = max(A[: len_a // 2])
max_A_r = max(A[len_a // 2:])

if max_A_l < max_A_r:
    print(A.index(max_A_l) + 1)
else:
    print(A.index(max_A_r, len_a // 2) + 1)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = 0
for a, b in zip(A, B):
    s += a * b

print('Yes' if s == 0 else 'No')
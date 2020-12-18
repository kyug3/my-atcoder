S, T = input().split()
A, B = map(int, input().split())
U = input()
print(f"{A - 1} {B}" if S == U else f"{A} {B - 1}")
A, B, C, D = map(int, input().split())
if A < C:
    print(max(0, min(B, D) - C))
else:
    print(max(0, min(B, D) - A))
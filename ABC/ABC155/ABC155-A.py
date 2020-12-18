A, B, C = map(int, input().split())
if A == B == C or (A != B and B != C and C != A):
    print('No')
else:
    print('Yes')
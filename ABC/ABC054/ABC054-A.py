A, B = map(int, input().split())
A = 14 if A == 1 else A
B = 14 if B == 1 else B
if A > B:
    print('Alice')
else:
    print('Draw' if A == B else 'Bob')
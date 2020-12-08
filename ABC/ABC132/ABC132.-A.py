import sys
input = sys.stdin.readline

S = list(input().rstrip())
set_S = set(S)

if len(set_S) == 2 and S.count(S[0]) == 2:
    print("Yes")
else:
    print("No")
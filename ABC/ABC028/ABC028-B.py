import sys
input = sys.stdin.readline

S = input().rstrip()
ans = ""

for w in ['A', 'B', 'C', 'D', 'E', 'F']:
    ans += str(S.count(w)) + ' '

print(ans.rstrip())
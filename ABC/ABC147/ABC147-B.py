import sys
input = sys.stdin.readline

S = input().rstrip()
a = S[:len(S) // 2]
if len(S) % 2 == 1:
    b = S[len(S) // 2 + 1:][::-1]
else:
    b = S[len(S) // 2:][::-1]
ans = 0
for x, y in zip(a, b):
    if x != y:
        ans += 1
print(ans)
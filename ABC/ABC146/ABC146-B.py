import sys
input = sys.stdin.readline

def func(c):
    x = ord(c) + N
    if x > 90:
        x -= 26
    return chr(x)

N = int(input())
S = input().rstrip()
ans = ""
for s in S:
    ans += func(s)
print(ans)
s = input()

x = len(s)
ans = 0
while x:
    x -= 2
    if s[: x//2] == s[x//2: x]:
        ans = x
        break
print(ans)
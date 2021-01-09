s = input()

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print(i + 1, i + 2)
        exit()
    if i + 2 == len(s):
        continue
    if s[i] == s[i + 2]:
        print(i + 1, i + 3)
        exit()
else:
    print(-1, -1)
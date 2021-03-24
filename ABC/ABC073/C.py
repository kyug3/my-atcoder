N = int(input())
s = set()
for _ in range(N):
    a = int(input())
    if a in s:
        s.remove(a)
    else:
        s.add(a)
print(len(s))
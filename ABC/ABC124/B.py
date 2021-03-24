N = int(input())
H = list(map(int, input().split()))

ans = 1
highest = H[0]
for h in H[1:]:
    if highest <= h:
        ans += 1
        highest = h
print(ans)
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
border = sum(A) / (4 * M)
popular = []
for a in A:
    if a < border:
        break
    popular.append(a)

print("Yes" if len(popular) >= M else "No")

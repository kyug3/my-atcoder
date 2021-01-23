H, W, M = map(int, input().split())
h_bucket = [0] * (10 ** 5 * 3 + 1)
w_bucket = [0] * (10 ** 5 * 3 + 1)
bomber = set()
for _ in range(M):
    h, w = map(int, input().split())
    h_bucket[h] += 1
    w_bucket[w] += 1
    bomber.add((h, w))

hm = max(h_bucket)
wm = max(w_bucket)
hidx = []
widx = []
for i in range(10 ** 5 * 3 + 1):
    if hm == h_bucket[i]:
        hidx.append(i)
    if wm == w_bucket[i]:
        widx.append(i)
ans = hm + wm
for i in hidx:
    for j in widx:
        if not (i, j) in bomber:
            print(ans)
            exit()
else:
    print(ans - 1)
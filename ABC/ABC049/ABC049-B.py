H, W = map(int, input().split())
image = []
for _ in range(H):
    C = list(input())
    image.append(C)
    image.append(C)

for i in image:
    print(''.join(i))
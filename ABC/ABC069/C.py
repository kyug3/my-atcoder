N = int(input())
A = list(map(int, input().split()))

two = 0
three = 0
four = 0
for a in A:
    if not a % 4:
        four += 1
    elif not a % 2:
        two = 1
    else:
        three += 1

print('Yes' if four >= two+three-1 else 'No')
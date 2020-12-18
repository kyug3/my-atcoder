N = int(input())
A = [n for n in map(int, input().split()) if n % 2 == 0]
for a in A:
    if a % 3 != 0 and a % 5 != 0:
        print('DENIED')
        break
else:
    print('APPROVED')
import sys
input = sys.stdin.readline

lst = []
for _ in range(5):
    lst.append(int(input()))
k = int(input())
for n in range(5):
    for m in range(n+1, 5):
        if abs(lst[n] - lst[m]) > k:
            print(':(')
            exit()
print('Yay!')
N = int(input())
A = list(map(int, input().split()))
pm = len([a for a in A if a < 0]) % 2
A = [abs(a) for a in A]

if pm:
    print(sum(A) - min(A) * 2)
else:
    print(sum(A))
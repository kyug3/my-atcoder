N = int(input())
A = list(map(int, input().split()))
setA = set(A)
print('YES' if len(A) == len(setA) else 'NO')
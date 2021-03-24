N = int(input())

lst = []
for i in range(1, N + 1):
    if i ** 2 > N:
        break
    if N % i == 0:
        lst.append(i)
        lst.append(N // i)

def F(a, b):
    a, b = str(a), str(b)
    return max(len(a), len(b))
    
print(F(lst[-1], lst[-2]))
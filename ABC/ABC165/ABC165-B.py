X = int(input())
n = 100
year = 0
while n < X:
    year += 1
    n += n // 100
print(year)
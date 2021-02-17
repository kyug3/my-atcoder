N = int(input())
t, a = 1, 1
for _ in range(N):
    tn, an = map(int, input().split())
    x = max((t + tn - 1) // tn, (a + an - 1) // an)
    t = tn * x
    a = an * x
print(t + a)

import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

#  0 0
#  1 1
# 10 -2
# 11 -1
# 100 4
# 101 5
# 110 2
# 111 3
# 1000 -8
# 1001 -7
# 1010 -10
# 1011 -9
# 1100 -4
# 1101 -3
# 1110 -6
# 1111 -5

# 桁数が奇数 -> 正
#      偶数 -> 負
# N桁目の範囲 N-2桁目の最大値 < N-2桁目の最大値 + 2**(N-1)
N = int(input())
if N == 0:
    print(0)
    exit()

def get_digit(N):
    c1, c2 = 0, 0
    for i in range(1, 100):
        if i % 2:
            c1 += (-2)**(i-1)
            if c1 >= N and N > 0:
                digit = i
                break
        else:
            c2 += (-2)**(i-1)
            if c2 <= N and N < 0:
                digit = i
                break
    return digit


d = get_digit(N)
ans = ['0'] * (d)
while N:
    digit = get_digit(N)
    N -= (-2) ** (digit-1)
    ans[digit-1] = '1'

print(int(''.join(ans[::-1])))

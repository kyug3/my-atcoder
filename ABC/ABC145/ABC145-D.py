import math

X, Y = map(int, input().split())
mod = 10 ** 9 + 7

xy = X + Y
if xy % 3 != 0:
    print(0)
    exit()

move = xy // 3
pattern = min(X, Y) % move

if abs(X - Y) > move:
    print(0)
    exit()

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

N = move
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = cmb(move,pattern,mod)
print(ans)
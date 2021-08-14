"""
https://atcoder.jp/contests/abc186/editorial/401
Ax = B mod M となる最小のxを求める問題
1. d = gcd(A, B, M) とし、A/d, B/d, M/d で置き換える
2. gcd(A, M) != 1 のとき解なし
3. gcd(A, M) = 1 のとき mod M における Aの逆元を A^-1とし x = A^-1 B が解
"""

def ext_gcd(a, b):
    """
    ax + by = gcd(a,b)
    を満たす gcd(a,b), x, y
    """
    if a == 0:
        return b, 0, 1
    g, y, x = ext_gcd(b % a, a)
    return g, x - (b // a) * y, y

def crt(b1, m1, b2, m2):
    """
    x = b1 (mod m1)
    x = b2 (mod m2)
    を満たすx
    """
    d, p, q = ext_gcd(m1, m2)
    if (b2 - b1) % d != 0:
        return -1
    m = m1 * (m2 // d)
    tmp = (b2 - b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r

print(ext_gcd(3, 7))
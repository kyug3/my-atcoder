mod = 998244353

def matpow(A, B, w):
    l = len(A)
    while w:
        if w & 1:
            C = [0] * l
            for i in range(l):
                for j in range(l):
                    C[i] += A[i][j] * B[j]
                    C[i] %= mod
            B = C

        C = [[0] * l for _ in range(l)]
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    C[i][j] += A[i][k] * A[k][j]
                    C[i][j] %= mod
        A = C
        w >>= 1
    return B
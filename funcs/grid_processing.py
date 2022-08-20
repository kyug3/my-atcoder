def rotate_clockwise(A):
    return list(zip(*(A[::-1])))

def rotate_counter_clockwise(A):
    return list(zip(*(A)))[::-1]
    
def trim_extra(A, rem='.'):
    for _ in range(4):
        A = rotate_clockwise(A)
        while all(x == rem for x in A[-1]):
            A.pop()
    return A

# こっちのほうがはやい
def rotate(X):
    h = len(X); w = len(X[0])
    NX = [[-1] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            NX[j][h-1-i] = X[i][j]
    return NX
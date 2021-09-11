def rotate_right(A):
    return list(zip(*(A[::-1])))
    
def trim_extra(A, rem='.'):
    for _ in range(4):
        A = rotate_right(A)
        while all(x == rem for x in A[-1]):
            A.pop()
    return A

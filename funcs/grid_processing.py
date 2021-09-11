def rotate_clock_wise(A):
    return list(zip(*(A[::-1])))

def rotate_counter_clock_wise(A):
    return list(zip(*(A)))[::-1]
    
def trim_extra(A, rem='.'):
    for _ in range(4):
        A = rotate_clock_wise(A)
        while all(x == rem for x in A[-1]):
            A.pop()
    return A

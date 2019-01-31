def insertion_sort(A):
    """ Insertion Sort from Chapter 1. """

    n = len(A)
    for j in range(1, n):
        i = j - 1
        key = A[j]
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


def insertion_sort_dec(A):
    """ nonincreasing version Insertion Sort from Exercises 2.1-2 Chapter 1. """

    n = len(A)
    for j in range(1, n):
        i = j-1
        key = A[j]
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


def linear_search(A, x):
    """ Linear Search from Exercises 2.1-3 Chapter 1. """

    for i in range(len(A)):
        if A[i] == x:
            return i
    return None


def binary_add(A, B):
    """ Binary Add from Exercises 2.1-4 Chapter 1. """

    #  Set sentinel.
    if len(A) != len(B):
        return "A & B do not have the same length"

    #  Allocate C as output list.
    n = len(A)
    C = [None] * (n + 1)

    flag = 0  # set flag as carry bit, initial value is 0.
    for i in range( n-1, -1, -1 ):
        tmp = A[i] + B[i] + flag
        C[i+1] = tmp % 2  #  Binary addition rule.
        if tmp > 1:       #  Reset carry value.
            flag = 1
        else:
            flag = 0
    C[0] = flag
    return C




if __name__ == "__main__":
    x = 6
    A1 = [5, 2, 4, 6, 1, 3]
    A2 = [1, 1, 0, 1]
    B2 = [1, 0, 1, 1]
    # print( insertion_sort(A1) )
    # print( insertion_sort_dec(A1) )
    # print( linear_search(A1, x) )
    print( binary_add(A2, B2) )


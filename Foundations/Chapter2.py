import  math

def insertion_sort(A):
    """ Insertion Sort from Chapter 2. """

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
    """ nonincreasing version Insertion Sort from Exercises 2.1-2 Chapter 2. """

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
    """ Linear Search from Exercises 2.1-3 Chapter 2. """

    for i in range(len(A)):
        if A[i] == x:
            return i
    return None


def binary_add(A, B):
    """ Binary Add from Exercises 2.1-4 Chapter 2. """

    #  Set sentinel.
    if len(A) != len(B):
        return "A & B do not have the same length."

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


def selection_sort(A):
    """ Selection Sort from Exercises 2.2-2 Chapter 2. """

    n = len(A)
    for i in range( 0, n - 1 ):
        minA = A[i]
        k = i
        for j in range( i+1, n ):
            if A[j] < minA:
                minA = A[j]
                k = j
        A[k] = A[i]
        A[i] = minA
    return A


def merge(A, p, q, r):
    """ The function used in merge sort in Chapter 2. """

    n1 = q - p + 1
    n2 = r - q
    L = [None]*(n1+1)
    R = [None]*(n2+1)
    for i in range(p, q+1):
        L[i-p] = A[i]
    for i in range(q+1, r+1):
        R[i-q-1] = A[i]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    """ Merge Sort from Chapter 2. """
    """ Since the special feature of list in Python, we do not need a return. """
    """ The A list changes automatically. """

    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge_sort_aux(A):
    """ Auxiliary function for Merge Sort in Chapter 2."""

    merge_sort(A, 0, len(A) - 1)
    return A


def merge_no_sentinel(A, p, q, r):
    """ Merge function from Exercises 2.3-2 Chapter 2. """
    """ Merge function without using sentinels. """

    n1 = q - p + 1
    n2 = r - q
    L = [None]*(n1)
    R = [None]*(n2)
    for i in range(p, q+1):
        L[i-p] = A[i]
    for i in range(q+1, r+1):
        R[i-q-1] = A[i]
    i = 0
    j = 0
    for k in range(p, r+1):
        #  L list has run out.
        if i == n1 and j < n2:
            A[k] = R[j]
            j += 1
        #  R list has run out.
        elif i < n1 and j == n2:
            A[k] = L[i]
            i += 1
        #  Otherwise.
        else:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1


def insert(A, n):
    """ Function used in Recursive insertion sort from Exercises 2.3-4 Chapter 2. """
    """ Insert A[n] to A[0,1, ... , n-1] which has already sorted. """

    key = A[n]
    j = n - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key


def insertion_sortRecu(A, n):
    """ Recursive insertion sort Chapter 2. """

    if n > 0:
        insertion_sortRecu(A, n - 1)
        insert(A, n)


def insertion_sortRecu_aux(A):
    """ Auxiliary function for Recursive Insertion Sort in Exercises 2.3-4 Chapter 2. """

    n = len(A)
    insertion_sortRecu(A, n - 1)
    return A


def binary_search_iter(A, x):
    """ Iterative Binary Search in Exercises 2.3-5 Chapter 2. """

    n = len(A)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end)//2
        if A[mid]  == x:
            return mid
        elif x < A[mid]:
            end = mid - 1
        else:   # x > A[mid]
            start = mid + 1
    return None


def binary_search_recur(A, start, end, x):
    """ Recursive Binary Search in Exercises 2.3-5 Chapter 2. """

    #  base case
    if start > end:
        return None

    mid = (start + end)//2
    #  base case
    if A[mid] == x:
        return mid

    if x < A[mid]:
        return binary_search_recur(A, start, mid - 1, x)
    else:
        return binary_search_recur(A, mid + 1, end, x)


def binary_searth_recu_aux(A, x):
    """ Auxiliary function for Recursive Binary Search in Exercises 2.3-5 Chapter 2. """
    n = len(A)
    return binary_search_recur(A, 0, n-1, x)


def exchange(x, y):
    """ Auxiliary function for Bubble Sort in Problems 2-2 Chapter 2. """
    """ Exchange the values of x and y without extra variable. """

    x = x + y
    y = x - y
    x = x - y
    return x, y


def bubble_sort(A):
    """ Bubble Sort in Problems 2-2 Chapter 2. """

    n = len(A)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = exchange(A[j], A[j-1])
    return(A)


def polynomial(A, x, n):
    """ Naive algorithm to compute polynomial in Problems 2-3 Chapter 2. """

    y = 1/x
    res = 0
    for i in range(n+1):
        y = y*x
        res += y*A[i]
    return res


def horner4ploy(A, x, n):
    """ Horner's rule to compute polynomial in Problems 2-3 Chapter 2. """

    y = 0
    for i in range(n, -1, -1):
        y = y*x + A[i]
    return y


def inversion_naive(A):
    """ The naive algorithm to compute inversions in list A. """
    """ Problems 2-4 Chapter 2. """

    n = len(A)
    inversions = 0
    for i in range( n-1 ):
        count = 0
        for j in range( i+1, n):
            if A[j] < A[i]:
                count += 1
        inversions += count
    return inversions


def inversion_merge(A, p, q, r):
    """ The function used in inversion_mergesort. """
    """ Problems 2-4 Chapter 2. """

    n1 = q - p + 1
    n2 = r - q
    L = [None]*(n1+1)
    R = [None]*(n2+1)
    for i in range(p, q+1):
        L[i-p] = A[i]
    for i in range(q+1, r+1):
        R[i-q-1] = A[i]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    inversion = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            inversion += 1
            A[k] = R[j]
            j += 1
    return inversion



def inversion_mergesort(A, p, r):
    """ Get the inversions in list A by using Merge Sort. """
    """ Problems 2-4 Chapter 2. """

    #  Base case
    if p == r:
        return 0
    elif p < r:
        q = (p + r)//2
        left_inver = inversion_mergesort(A, p, q)
        right_inver = inversion_mergesort(A, q+1, r)
        return  inversion_merge(A, p, q, r) + left_inver + right_inver


def inversion_mergesort_aux(A):
    """ Auxiliary function for inversion_mergesort in Problems 2-4 Chapter 2. """

    n = len(A)
    return inversion_mergesort(A, 0, n-1)



if __name__ == "__main__":
    #  Test Data.
    x = 6
    A1 = [5, 2, 4, 6, 1, 3]
    A2 = [1, 1, 0, 1]
    B2 = [1, 0, 1, 1]
    A3 = [2, 4, 5, 7, 1, 2, 3, 6]
    A4 = [1, 2, 3, 4, 5, 6, 7, 8]
    A5 = [0,1,2,3,4]
    A6 = [2, 3, 8, 6, 1]

    #  All the test result.
    print( insertion_sort(A1) )
    print( insertion_sort_dec(A1) )
    print( linear_search(A1, x) )
    print( binary_add(A2, B2) )
    print( selection_sort(A1) )
    print( merge_sort_aux(A3) )
    print( insertion_sortRecu_aux(A1) )
    print( binary_search_iter(A4, 1) )
    print( binary_searth_recu_aux(A4, 1) )
    print( bubble_sort(A1) )
    print( polynomial(A5, 2, 4) )
    print( horner4ploy(A5, 2, 4) )
    print( inversion_naive(A6) )
    print( inversion_mergesort_aux(A6) )
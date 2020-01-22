def selection_sort(A):
    for i in range(len(A) - 1):
        mmin = A[i]
        ind = i
        for j in range(i, len(A)):
            if A[j] < mmin:
                mmin = A[j]
                ind = j
        if ind != i:
            A[i], A[ind] = A[ind], A[i]
    return A
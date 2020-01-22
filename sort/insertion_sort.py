def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        cur = A[i]
        loc = i
        for j in range(i):
            if A[j] > A[i]:
                loc = j
                break
        for j in range(i, loc, -1):
            A[j] = A[j-1]
        A[loc] = cur
    return A

## 代码需要修改
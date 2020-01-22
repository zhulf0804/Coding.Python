import random


def helper(A, l, r):
    if l >= r:
        return
    pivot = random.choice(range(l, r+1))
    pivot_val = A[pivot]
    cur = l
    A[r], A[pivot] = pivot_val, A[r]
    for i in range(l,  r):
        if A[i] <= pivot_val:
            A[i], A[cur] = A[cur], A[i]
            cur += 1
    A[cur], A[r] = A[r], A[cur]
    helper(A, l, cur-1)
    helper(A, cur+1, r)


def quick_sort(A):
    n = len(A)
    helper(A, 0, n-1)


A = [2, 3, 3, 1]
quick_sort(A)
print(A)
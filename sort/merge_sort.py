def helper(A, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    helper(A, l, mid)
    helper(A, mid + 1, r)
    i, j = l, mid + 1
    tmp = list(A)
    cur = l
    while i <= mid and j <= r:
        if tmp[i] <= tmp[j]:
            A[cur] = tmp[i]
            i += 1
        else:
            A[cur] = tmp[j]
            j += 1
        cur += 1
    if i <= mid:
        A[cur:r + 1] = tmp[i:mid + 1]
    if j <= r:
        A[cur:r + 1] = tmp[j:r + 1]


def merge_sort(A):
    n = len(A)
    helper(A, 0, n - 1)

## 上述代码在lintcode上面提交TLE，通过了%83的测试用例
## 下述代码做了部分优化，就ac了


## 以下为ac代码
# 当数组规模比较小的时候，改用插入排序
'''
def insertion_sort(A, l, r):
    for i in range(l+1, r+1):
        cur = A[i]
        loc = i
        for j in range(l, i):
            if A[j] > A[i]:
                loc = j
                break
        for j in range(i, loc, -1):
            A[j] = A[j-1]
        A[loc] = cur
    return A


def helper(A, l, r):
    if r - l <= 100:
        insertion_sort(A, l, r)
        return
    mid = (l + r) // 2
    helper(A, l, mid)
    helper(A, mid + 1, r)
    i, j = l, mid + 1
    tmp = list(A)
    cur = l
    while i <= mid and j <= r:
        if tmp[i] <= tmp[j]:
            A[cur] = tmp[i]
            i += 1
        else:
            A[cur] = tmp[j]
            j += 1
        cur += 1
    if i <= mid:
        A[cur:r+1] = tmp[i:mid+1]
    if j <= r:
        A[cur:r+1] = tmp[j:r+1]


def merge_sort(A):
    n = len(A)
    helper(A, 0, n-1)


A = list(range(100000))
merge_sort(A)
'''
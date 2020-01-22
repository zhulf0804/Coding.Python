def shell_sort(A):
    n = len(A)
    d = n // 2
    while d:
        for st in range(d):
            for cur in range(st+d, n, d):
                pre = cur - d
                cur_val = A[cur]
                while pre >= 0  and A[pre] > cur_val:
                    pre -= d
                for j in range(cur, pre + d, -d):
                    A[j] = A[j - d]
                A[pre + d] = cur_val
                #print(st, d, A)
        #print(d, A)
        d = d // 2
A = [2, 3, 5, 1]
shell_sort(A)
print(A)
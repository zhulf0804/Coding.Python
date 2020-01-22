n, k = list(map(int, input().strip().split()))

counts = [[0]*n for i in range(n)]
grids = []


def helper(arr, k):
    n = len(arr)
    st, cur = 0, 0
    res = [0] * n
    while cur < n:
        if arr[cur] == '.':
            cur += 1
        else:
            length = cur - st
            if length >= k:
                mmax = min(length - k  + 1, k)
                i, j = st, cur - 1
                cnt = 1
                while i <= j:
                    res[i] = min(mmax, cnt)
                    res[j] = min(mmax, cnt)
                    cnt += 1
                    i += 1
                    j -= 1
            st = cur + 1
            cur = st
    if arr[cur - 1] == '.':
        length = cur - st
        if length >= k:
            mmax = min(length - k + 1, k)
            i, j = st, cur - 1
            cnt = 1
            while i <= j:
                res[i] = min(mmax, cnt)
                res[j] = min(mmax, cnt)
                cnt += 1
                i += 1
                j -= 1
    return res


for i in range(n):
    line = input().strip()
    grids.append(line)
    res = helper(line, k)
    for j in range(len(res)):
        counts[i][j] += res[j]

mmax = 0
x, y = 1, 1
for i in range(n):
    line = []
    for j in range(n):
        line.append(grids[j][i])
    res = helper(line, k)
    for j in range(len(res)):
        counts[j][i] += res[j]
        if counts[j][i] > mmax:
            mmax = counts[j][i]
            x, y = j + 1, i + 1
print(x, y)
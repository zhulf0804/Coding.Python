n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
t = list(map(int, input().split()))


locs = []
for i in range(n + m):
    if t[i] == 1:
        locs.append(i)

res = [0] * m
res[0] += locs[0]
res[-1] += n + m - 1 - locs[-1]


def helper(l, r, a, b):
    z = l
    while l < r:
        mid = l + (r - l + 1) // 2
        if x[mid] - a <= b - x[mid]:
            l = mid
        else:
            r = mid - 1

    if x[l] - a <= b - x[l]:
        return l - z + 1
    else:
        return 0


for i in range(1, m):
    cur = locs[i]
    pre = locs[i-1]
    if pre == cur - 1:
        continue
    a, b = x[pre], x[cur]
    num = helper(pre + 1, cur - 1, a, b)
    res[i-1] += num
    res[i] += (cur - pre - 1 - num)

print(' '.join(map(str, res)))
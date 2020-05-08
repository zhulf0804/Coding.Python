# 此题目重点在于规律
# helper是二分实现
# helper2是遍历实现
# 二分法比遍历更慢, (lmin, lmax, lmin, lmax, ...)
n, T = list(map(int, input().split()))
a = list(map(int, input().split()))

summ = []
cur = 0
mmin = a[0]
for item in a:
    cur += item
    summ.append(cur)
    mmin = min(item, mmin)

def helper(x, l, r=n-1):
    z = l
    while l < r:
        mid = (l + r) // 2
        cur = summ[mid] - summ[z] + a[z]
        if cur <= x:
            l = mid + 1
        else:
            r = mid
    if summ[l] - summ[z] + a[z]  > x:
        return l
    else:
        return l + 1

def helper2(x, l, r=n-1):
    cur = l
    while cur <= r and summ[cur] - summ[l] + a[l] <= x:
        cur += 1
    return cur


ans = 0
left = T
d = {}
while T >= mmin:
    l = 0
    t, num = 0, 0
    left = T
    while left >= mmin and l < n:
        r = helper2(left, l)
        if l == r:
            l += 1
            continue
        t += summ[r - 1] - summ[l] + a[l]
        num += (r - l)
        left -= (summ[r - 1] - summ[l] + a[l])
        l = r + 1
    ans += (T // t) * num
    #print(t, num, ans)
    T = T % t
print(ans)

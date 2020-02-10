n, q = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
k = list(map(int, input().strip().split()))
summ = []
cur = 0
for item in a:
    cur += item
    summ.append(cur)


def find_loc(l, val, r, nums, target):
    l0 = l
    while l < r:
        mid = (l + r) // 2
        cur_add = nums[mid] - nums[l0] + val
        if cur_add <= target:
            l = mid + 1
        else:
            r = mid
    if nums[l] - nums[l0] + val > target:
        return l, nums[l] - nums[l0] + val - target
    else:
        return l + 1, nums[0]


st = 0
cur = summ[0]
for item in k:
    loc, cur = find_loc(st, cur, n-1, summ, item)
    if loc == n:
        print(n)
        st = 0
    else:
        print(n-loc)
        st = loc
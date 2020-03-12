n, m, q = list(map(int, input().strip().split()))
s = input()
t = input()
locs = []
for i in range(n):
    if i + m <= n and s[i:i+m] == t:
        locs.append(i)

#print(locs)
def find_max(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    if nums[l] >= target:
        return l
    else:
        return len(nums)

def helper(l, r, nums):
    if len(nums) == 0:
        return 0
    x = find_max(nums, l)
    y = find_max(nums, r)
    if y >= len(nums) or nums[y] > r:
        return y - x
    else:
        return y - x + 1


for i in range(q):
    l, r = list(map(int, input().strip().split()))
    l -= 1
    r -= 1
    if r - m + 1 < l:
        print(0)
    else:
        res = helper(l, r - m + 1, locs)
        print(res)
# https://nanti.jisuanke.com/t/T1158
n = int(input())
nums = list(map(int, input().strip().split()))
nums.sort()
m = int(input())
l, r = 0, n - 1
ok = True
while l < r:
    cur = nums[l] + nums[r]
    if cur == m:
        print(nums[l], nums[r])
        ok = False
        break
    elif cur < m:
        l += 1
    else:
        r -= 1
if ok:
    print("No")
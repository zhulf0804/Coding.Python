n, k = list(map(int, input().strip().split()))
nums = list(map(int, input().strip().split()))
nums = sorted(nums)

if k == 0:
    if nums[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n:
    if nums[k-1] <= 1e9:
        print(nums[k-1])
    else:
        print(-1)
else:
    if nums[k-1] == nums[k]:
        print(-1)
    else:
        print(nums[k-1])
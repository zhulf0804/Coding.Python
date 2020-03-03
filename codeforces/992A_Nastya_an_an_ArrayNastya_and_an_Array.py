n = int(input())
nums = list(map(int, input().strip().split()))

nums = set(nums)
if 0 in nums:
    print(len(nums) - 1)
else:
    print(len(nums))
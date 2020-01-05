import bisect

line = input()
n, d = int(line.strip().split()[0]), int(line.strip().split()[1])

line = input()
nums = [int(item) for item in line.strip().split()]
nums = sorted(nums)

maxd = 0
for i in range(n):
    st = nums[i]
    end = nums[i] + d
    loc = bisect.bisect_right(nums, end)
    #print(i, loc)
    dd = loc - i
    maxd = max(maxd, dd)
print(n - maxd)
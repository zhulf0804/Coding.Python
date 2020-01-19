n = int(input())
nums = list(map(int, input().strip().split()))
#print(n)
#print(nums)
summ = 0
for item in nums:
    summ += item

res = 0
cur = 0
for i in range(len(nums)):
    cur += nums[i]
    if cur >= summ / 2:
        res = i
        break
print(res + 1)

## 二分查找
#summ = []
#for item in nums:

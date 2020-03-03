n = int(input())
nums = list(map(int, input().strip().split()))

mmin = float('inf')
res = 1
for i in range(n):
    cur = nums[i] - i
    if cur <= 0:
        res = i + 1
        break
    cur = 1 + (cur - 1) // n
    if cur < mmin:
        mmin = cur
        res = i + 1
print(res)
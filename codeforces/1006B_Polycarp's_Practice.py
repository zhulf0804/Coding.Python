n, k = list(map(int, input().strip().split()))
nums = list(map(int, input().strip().split()))

sorted_nums = sorted(nums)
needed = {}
summ = 0
for i in range(n-1, n-1-k, -1):
    cur = sorted_nums[i]
    summ += cur
    needed[cur] = needed.get(cur, 0) + 1
print(summ)
loc = []
for i in range(n):
    cur = nums[i]
    if needed.get(cur, 0) != 0:
        loc.append(i)
        needed[cur] -= 1

res = []
left = 0
for i in range(len(loc) - 1):
    res.append(str(loc[i] - left + 1))
    left = loc[i] + 1
res.append(str(n - left))
print(' '.join(res))
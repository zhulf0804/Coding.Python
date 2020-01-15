n, m = list(map(int, input().strip().split(' ')))
nums = list(map(int, input().strip().split(' ')))

#print(n, m)
#print(nums)
res = 0
count = [0] * n
for item in nums:
    count[item-1] += 1
    ok = True
    for i in range(n):
        if count[i] == 0:
            ok = False
            continue
    if ok:
        res += 1
        for i in range(n):
            count[i] -= 1

print(res)

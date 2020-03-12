n, m = list(map(int, input().strip().split()))
nums = list(map(int, input().strip().split()))

res = []
pre = 0
for i in range(n):
    cur = nums[i]
    if cur + pre < m:
        res.append('0')
        pre += cur
    else:
        z1 = (cur + pre) // m
        z2 = (cur + pre) % m
        res.append(str(z1))
        pre = z2
print(" ".join(res))

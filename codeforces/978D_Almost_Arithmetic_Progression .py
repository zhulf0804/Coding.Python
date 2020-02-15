n = int(input())
nums = list(map(int, input().strip().split()))

if len(nums) <= 2:
    print(0)
else:
    res = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            ok = True
            tmp = abs(i) + abs(j)
            a = nums[0] + i
            b = nums[1] + j
            d = b - a
            pre = b
            for k in range(2, n):
                cur = pre + d
                if abs(cur - nums[k]) > 1:
                    ok = False
                    break
                else:
                    tmp += abs(cur - nums[k])
                    pre = cur
            if ok:
                res.append(tmp)
    if len(res) == 0:
        print(-1)
    else:
        print(min(res))
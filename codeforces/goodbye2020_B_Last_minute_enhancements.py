t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    nums = list(map(int, input().split()))
    ans, pre = 1, nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num == pre:
            ans += 1
            pre = num + 1
        elif num > pre:
            pre = num
            ans += 1
    print(ans)
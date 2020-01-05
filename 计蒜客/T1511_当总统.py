n = int(input())
while n:
    line = input()
    nums = [int(item) for item in line.strip().split()]
    #print(nums)
    k = n // 2 + 1
    nums = sorted(nums)
    res = 0
    for i in range(k):
        cur = nums[i] // 2 + 1
        res += cur
    print(res)
    n = int(input())
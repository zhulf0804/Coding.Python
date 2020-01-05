t = int(input())
for i in range(t):
    line = input()
    n, s = list(map(int, line.strip().split()))
    line = input()
    nums = list(map(int, line.strip().split()))
    #print(n, s)
    #print(nums)
    summ = 0
    i = 0
    mmax = -1
    mmax_idx = -1
    while summ <= s and i < n:
        summ += nums[i]
        if nums[i] > mmax:
            mmax = nums[i]
            mmax_idx = i
        i += 1

    if summ <= s:
        print(0)
        continue
    print(mmax_idx + 1)

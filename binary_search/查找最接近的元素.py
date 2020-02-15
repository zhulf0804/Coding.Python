# https://nanti.jisuanke.com/t/T1156

n = int(input())
nums = list(map(int, input().strip().split()))
m = int(input())


def find(x):
    # 第一个大于等于 x 的索引
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < x:
            l = mid + 1
        else:
            r = mid

    if nums[l] < x:
        return l + 1
    else:
        return l


for i in range(m):
    x = int(input())
    ind = find(x)
    if ind == 0:
        print(nums[ind])
    elif ind == n:
        print(nums[ind - 1])
    else:
        if abs(nums[ind] - x) < abs(nums[ind - 1] - x):
            print(nums[ind])
        else:
            print(nums[ind - 1])
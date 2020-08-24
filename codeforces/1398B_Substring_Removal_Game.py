T = int(input())

for _ in range(T):
    s = input()
    n = len(s)
    pre, cur, nums = -1, 0, []
    while cur < n:
        if s[cur] == '1' and (cur + 1 == n or s[cur+1] == '0'):
            nums.append(cur - pre)
        if s[cur] == '0' and cur + 1 < n and s[cur + 1] == '1':
            pre = cur
        cur += 1
    nums = sorted(nums, reverse=True)
    i, ans = 0, 0
    while i < len(nums):
        ans += nums[i]
        i += 2
    print(ans)
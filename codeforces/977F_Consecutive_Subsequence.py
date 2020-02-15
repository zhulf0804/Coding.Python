#import random
n = int(input())
nums = list(map(int, input().strip().split()))
#n = 200000
#nums = [random.randint(0, int(1e9)) for _ in range(n)]
#nums = list(range(n))
#print(nums)

d = {}
pre = {}
loc = {}
for i in range(n):
    cur = nums[i]
    loc[cur] = i + 1
    if cur - 1 in d:
        d[cur] = d[cur - 1] + 1
        pre[i + 1] = loc[cur - 1]
    else:
        d[cur] = 1

mmax = 0
mmax_val = 0
for key, val in d.items():
    if val > mmax:
        mmax = val
        mmax_val = key
print(mmax)
i = loc[mmax_val]
res = [str(i)]
#print(nums[i-1])
while i in pre:
    j = pre[i]
    #print(nums[j-1])
    res.append(str(j))
    i = j
res.reverse()
print(" ".join(res))
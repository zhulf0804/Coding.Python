line = input()
N, K = int(line.strip().split()[0]), int(line.strip().split()[1])
line = input()
nums = [int(item) for item in line.strip().split()]
#print(N, K)
#print(nums)
mmax = -1
k = -1
for i in range(K):
    cap = nums[i]
    cur = (N // cap) * cap
    if cur > mmax:
        mmax = cur
        k = i
print(k + 1, N // nums[k])
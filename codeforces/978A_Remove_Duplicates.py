n = int(input())
nums = input().strip().split()
nums.reverse()
res = []
d = {}
for item in nums:
    #print(item)
    if item not in d:
        d[item] = 1
        res.append(item)
res.reverse()
print(len(res))
print(" ".join(res))
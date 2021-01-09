t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    nums = list(map(int, input().split()))
    areas = []
    for i in range(n):
        for j in range(i+1, n):
            area = nums[j] - nums[i]
            areas.append(area)
    print(len(set(areas)))

n = int(input())
line = input()
nums = [int(item) for item in line.strip().split()]
#print(nums)
nums.insert(0, 0)
#print(nums)
exist = False
for i in range(1, n+1):
    num1 = i
    num2 = nums[num1]
    if num1 == num2:
        continue
    num3 = nums[num2]
    if num1 == nums[num3]:
        exist = True
        break
if exist:
    print("YES")
else:
    print("NO")
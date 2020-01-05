n = int(input())
line = input()
nums = list(map(int, line.strip().split()))
#print(n)
#print(nums)
A, B = 0, 0
for item in nums:
    if item >= 0:
        A += item
    else:
        B += item
print(A - B)
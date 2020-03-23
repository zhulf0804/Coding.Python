n = int(input())
nums = list(map(int, input().split()))
summ = 0
for num in nums:
    summ += num

if summ > 0:
    print("HARD")
else:
    print("EASY")
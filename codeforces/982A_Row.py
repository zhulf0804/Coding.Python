n = int(input())
seating = input()
l = 0
ok = True
for i in range(n):
    if seating[i] == '1':
        l = i + 1
        if i < n - 1 and seating[i + 1] == '1':
            print("No")
            ok = False
            break
    else:
        nums = i - l + 1
        if nums >= 3 or (i == n - 1 and nums == 2) or (i == 1 and nums == 2) or (n == 1 and nums == 1):
            print("No")
            ok = False
            break
if ok:
    print("Yes")
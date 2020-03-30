n = int(input())
a = input()
b = input()

res = 0
pre = False
for i in range(n):
    if a[i] == b[i]:
        if pre:
            res += 1
            pre = False
    else:
        if not pre:
            pre = True
        else:
            if a[i-1] == a[i]:
                res += 1
                pre = True
            else:
                res += 1
                pre = False
if pre:
    res += 1

print(res)
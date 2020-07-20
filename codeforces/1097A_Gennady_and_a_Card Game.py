a = input()
bs = input().split()
ok = False
for i in range(5):
    b = bs[i]
    if b[0] == a[0] or b[1] == a[1]:
        ok = True
        break
if ok:
    print("YES")
else:
    print("NO")
n = int(input())
strs = []
for i in range(n):
    strs.append(input())

strs = sorted(strs, key=lambda x:len(x))

ok = True
for i in range(n-1):
    if strs[i] not in strs[i+1]:
        print("NO")
        ok = False
        break
if ok:
    print("YES")
    for i in range(n):
        print(strs[i])
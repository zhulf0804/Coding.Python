n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a[0] == 0:
    print("NO")
elif a[s-1] == 1:
    print("YES")
else:
    if b[s-1] == 0:
        print("NO")
    else:
        ok = False
        for i in range(s, n):
            if a[i] == 1 and b[i] == 1:
                ok = True
                break
        if ok:
            print("YES")
        else:
            print("NO")
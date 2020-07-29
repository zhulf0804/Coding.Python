w, h = list(map(int, input().split()))
u1, d1 = list(map(int, input().split()))
u2, d2 = list(map(int, input().split()))

ans = w
while h > 0:
    ans += h
    if h == d1:
        ans = max(0, ans - u1)
    elif h == d2:
        ans = max(0, ans - u2)
    h -= 1

print(ans)
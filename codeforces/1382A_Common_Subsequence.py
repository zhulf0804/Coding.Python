t = int(input())
for _ in range(t):
    m, n = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = -1
    for i in range(1, 1001):
        if i in a and i in b:
            ans = i
            break
    if ans == -1:
        print("NO")
    else:
        print("YES")
        print(1, ans)
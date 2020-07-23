t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = n
    for i in range(n):
        if a[i] != 1:
            ans = i
            break
    if (ans == n and ans % 2 == 1) or (ans < n and ans % 2 == 0):
        print("First")
    else:
        print("Second")
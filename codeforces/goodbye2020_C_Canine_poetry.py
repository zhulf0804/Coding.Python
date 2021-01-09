t = int(input())
while t > 0:
    t -= 1
    s = input()
    n, arr = len(s), [v for v in s]
    ans = 0
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            arr[i] = '1'
            ans += 1
        elif i > 1 and arr[i] == arr[i-2]:
            arr[i] = '1'
            ans += 1
    print(ans)

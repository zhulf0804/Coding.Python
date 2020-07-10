for _ in range(int(input())):
    arg = 2 * int(input())
    l = 3
    ans = -1
    while l <= 360:
        degree = 360 / l
        if arg % degree == 0 and arg // degree != l - 1:
            ans = l
            break
        l += 1
    print(ans)
t = int(input())
for _ in range(t):
    a, b, k = list(map(int, input().split()))
    ans = (k // 2) * (a - b)
    if k % 2 != 0:
        ans += a
    print(ans)
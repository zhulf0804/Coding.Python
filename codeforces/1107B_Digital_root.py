n = int(input())
for _ in range(n):
    k, x = list(map(int, input().split()))
    ans = (k - 1) * 9 + x
    print(ans)
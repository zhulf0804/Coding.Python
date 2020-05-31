import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    ans = (r - l + 1) // 2
    if l % 2 == 0:
        ans *= -1
    if (r - l + 1) % 2 == 1:
        ans += (r * (-1) ** r)
    print(ans)
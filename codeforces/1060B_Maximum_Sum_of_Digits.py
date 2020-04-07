n = int(input())


def helper(k):
    res = 0
    while k > 0:
        remainder = k % 10
        k = k // 10
        res += remainder
    return res

ans = helper(n)

st = 9
while st <= n:
    cur = helper(st) + helper(n - st)
    ans = max(cur, ans)
    st = st * 10 + 9
print(ans)
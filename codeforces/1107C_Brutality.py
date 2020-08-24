n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = input()

l, r, ans = 0, 0, 0
cnt, summ = 0, []
while r < n:
    if s[r] != s[l]:
        #[l, ..., r-1]
        if r - l <= k:
            for i in range(l, r):
                ans += a[i]
        else:
            tmp = sorted(a[l:r], reverse=True)
            for i in range(k):
                ans += tmp[i]
        l = r
    r += 1

if r - l <= k:
    for i in range(l, r):
        ans += a[i]
else:
    tmp = sorted(a[l:r], reverse=True)
    for i in range(k):
        ans += tmp[i]
print(ans)
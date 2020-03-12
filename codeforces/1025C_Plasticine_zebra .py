s = input()
n = len(s)
dp = [1] * n
cur = s[-1]
end = n - 1
for i in range(n-1):
    if s[i] == cur:
        end = i
        break
    cur = s[i]
dp[n-1] = end + 1
res = dp[n-1]
for i in range(n-2, -1, -1):
    if s[i] != s[i+1]:
        dp[i] = min(n, 1 + dp[i + 1])
        res = max(dp[i], res)
    #print(i, s[i], dp[i])
#print(end + 1)
print(res)
# https://codeforces.com/problemset/problem/1096/D

n = int(input())
a = input()
w = list(map(int, input().split()))

dp = [[0] * 4 for _ in range(n + 1)]
if a[-1] == 'd':
    dp[-2][3] = w[-1]
l = [n] * 4
d = {'h': 0, 'a': 1, 'r': 2, 'd': 3}

for i in range(n-2, -1, -1):
    ind = d.get(a[i], -1)
    for j in range(4):
        dp[i] = dp[i + 1]
        if j == ind:
            if j <= 2:
                dp[i][j] = min(w[i] + dp[l[j]][j], dp[i+1][j+1])
            else:
                dp[i][j] = w[i] + dp[i+1][j]
            l[j] = i
print(dp[0][0])

'''
n = int(input())
a = input()
w = list(map(int, input().split()))

dp = [[float('inf')] * 4 for _ in range(n)]
hl, al, rl, dl = n, n , n, n

dp[-1][0], dp[-1][1], dp[-1][2], dp[-1][3] = 0, 0, 0, 0
if a[-1] == 'd':
    dp[-1][3] = w[-1]

for i in range(n-2, -1, -1):
    ch = a[i]
    delta = 0
    if ch == 'h':
        if hl < n:
            delta = dp[hl][0]
        dp[i][0] = min(w[i] + delta, dp[i+1][1])
        dp[i][1], dp[i][2], dp[i][3] = dp[i+1][1], dp[i+1][2], dp[i+1][3]
        hl = i
    elif ch == 'a':
        if al < n:
            delta = dp[al][1]
        dp[i][1] = min(w[i] + delta, dp[i+1][2])
        dp[i][0], dp[i][2], dp[i][3] = dp[i+1][0], dp[i+1][2], dp[i+1][3]
        al = i
    elif ch == 'r':
        if rl < n:
            delta = dp[rl][2]
        dp[i][2] = min(w[i] + delta, dp[i+1][3])
        dp[i][0], dp[i][1], dp[i][3] = dp[i+1][0], dp[i+1][1], dp[i+1][3]
        rl = i
    elif ch == 'd':
        dp[i][3] = w[i] + dp[i+1][3]
        dp[i][0], dp[i][1], dp[i][2] = dp[i+1][0], dp[i+1][1], dp[i+1][2]
        dl = i
    else:
        dp[i][0], dp[i][1], dp[i][2], dp[i][3] = dp[i+1][0], dp[i+1][1], dp[i+1][2], dp[i+1][3]
    #print(i, dp[i])

print(dp[0][0])
'''
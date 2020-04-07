import sys
input=sys.stdin.readline


N, L, M = list(map(int, input().split()))
ans = 0
cur = 0
for i in range(N):
    t, l = list(map(int, input().split()))
    ans += (t - cur) // M
    cur = t + l

ans += ((L - cur) // M)
print(ans)
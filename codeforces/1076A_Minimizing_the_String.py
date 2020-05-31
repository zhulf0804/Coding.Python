n = int(input())
s = input()

cur = -1
for i in range(n-2, -1, -1):
    if s[i] > s[i+1]:
        #print(i, s[i], s[i+1])
        cur = i

if cur == -1:
    print(s[:n-1])
else:
    print(s[:cur] + s[cur+1:])
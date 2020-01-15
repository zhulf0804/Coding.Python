n = int(input())
s = input()

if n <= 2 and '?' in s:
    print("Yes")
else:
    mmax = 0
    if s[0] == '?' or s[-1] == '?':
        mmax = 2
    for i in range(1, n-1):
        if s[i] == '?':
            if s[i-1] == '?' or s[i+1] == '?' or s[i-1] == s[i+1]:
                mmax = 2
        else:
            if s[i] == s[i-1] or s[i] == s[i+1]:
                mmax = 0
                break
    if mmax == 2:
        print("Yes")
    else:
        print("No")

n, k = list(map(int, input().split()))
s = input()

def helper(s):
    l = len(s)
    for i in range(1, l):
        if s[i:] == s[:(l - i)]:
            return l - i
    return 0

st = helper(s)

res = s
for i in range(k-1):
    res += s[st:]
print(res)
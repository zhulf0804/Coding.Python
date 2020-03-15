T = int(input())


def helper(s):
    flag = True
    for i in range(len(s) // 2):
        j = len(s) - i - 1
        if abs(ord(s[i]) - ord(s[j])) != 0 and abs(ord(s[i]) - ord(s[j])) != 2:
            flag = False
            break
    return flag


for i in range(T):
    n = int(input())
    s = input()
    flag = helper(s)
    if flag:
        print("YES")
    else:
        print("NO")
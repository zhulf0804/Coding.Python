from collections import Counter
n = int(input())

def func(s1, s2):
    l1, l2 = len(s1), len(s2)
    cs1 = Counter(s1)
    for i in range(l2):
        if i + l1 > l2:
            continue
        if Counter(cs1) == Counter(s2[i:i+l1]):
            return True
    return False

for i in range(n):
    p = input()
    pp = input()
    if len(p) > len(pp):
        print("NO")
        continue
    if func(p, pp):
        print("YES")
    else:
        print("NO")
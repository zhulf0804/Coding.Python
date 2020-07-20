n = int(input())
degs = [int(input()) for _ in range(n)]
def helper(cur, i):
    if i == n:
        #print(cur)
        if cur % 360 == 0:
            return True
        return False
    ok1 = helper(cur + degs[i], i+1)
    ok2 = helper(cur - degs[i], i+1)
    return ok1 or ok2
ok = helper(0, 0)
if ok:
    print("YES")
else:
    print("NO")
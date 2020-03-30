# https://nanti.jisuanke.com/t/T1406
n, r = list(map(int, input().split()))


def helper(cur, count):
    if count == r:
        return cur
    

helper([], 0)
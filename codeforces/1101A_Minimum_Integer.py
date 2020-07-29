q = int(input())
for _ in range(q):
    l, r, d = list(map(int, input().split()))
    if l > d:
        print(d)
    else:
        print((r // d + 1) * d)
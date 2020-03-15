import sys
input=sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    d = {}
    lens = []
    nums = list(map(int, input().strip().split()))
    for num in nums:
        d[num] = d.get(num, 0) + 1
        if d[num] == 2:
            lens.append(num)
            d[num] = 0
    lens = sorted(lens)
    a, b = lens[0], lens[1]
    mmin = float('inf')
    for i in range(1, len(lens)):
        if lens[i] / lens[i-1] < mmin:
            mmin = lens[i] / lens[i-1]
            a = lens[i]
            b = lens[i-1]
    print(a, a, b, b)
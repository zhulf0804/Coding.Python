n, s = list(map(int, input().strip().split()))
schd = []
for i in range(n):
    h, m = list(map(int, input().strip().split()))
    schd.append([h, m])

h, m = schd[0]
take_off_m = (s + 1) % 60
take_off_h = (s + 1) // 60
if take_off_h < h or (take_off_h == h and take_off_m <= m):
    print(0, 0)
else:
    find = False
    for i in range(n-1):
        h, m = schd[i]
        take_off_m = (m + 2*s + 2) % 60
        take_off_h = h + (m + 2*s + 2) // 60
        next_h, next_m = schd[i+1]
        if take_off_h < next_h or (take_off_h == next_h and take_off_m <= next_m):
            take_off_m = (m + s + 1) % 60
            take_off_h = h + (m + s + 1) // 60
            print(take_off_h, take_off_m)
            find = True
            break

    if not find:
        h, m = schd[-1]
        take_off_m = (m + s + 1) % 60
        take_off_h = h + (m + s + 1) // 60
        print(take_off_h, take_off_m)



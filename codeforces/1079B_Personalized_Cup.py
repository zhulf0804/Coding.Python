s = input()
l = len(s)
minr, minc = 5, 20
ok = False
for row in range(1, 6):
    if l > row * 20:
        continue
    if l == row * 20:
        minr = row
        minc = 20
        break
    for col in range(1, 21):
        if l > row * col:
            continue
        minr = row
        minc = col
        ok = True
        break
    if ok:
        break

print(minr, minc)
diff = minr * minc - l
c = 0
for i in range(minr):
    upper = minc
    app = ''
    if diff > 0:
        upper = minc - 1
        diff -= 1
        app = '*'
    print(s[c:c+upper] + app)
    c += upper
s = input()
nz = [0, 0]

locz = [
        [[1, 1], [1, 2], [1, 3], [1, 4]],
        [[3, 1], [3, 3], [4, 1], [4, 3]]
        ]

for item in s:
    ind = int(item)
    print(' '.join(map(str, locz[ind][nz[ind]])))
    nz[ind] += 1
    nz[ind] %= 4
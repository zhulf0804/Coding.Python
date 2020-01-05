from collections import defaultdict
num = int(input())
d = defaultdict(list)
for i in range(num):
    line = input()
    name, month, day = line.strip().split()
    key = month + '_' + day
    d[key].append(name)

exist = False
#d = sorted(d, key=lambda val: (int(val[0].split('_')[0]), int(val[0].split('_')[1])))
#d = sorted(d.iteritms(), key=lambda val: val[0])
keys = sorted(d.keys(), key=lambda val: (int(val.split('_')[0]), int(val.split('_')[1])))
#print(keys)
#print(d)
for key in keys:
    val = d[key]
    if len(val) > 1:
        exist = True
        val = sorted(val, key=lambda item: (len(item), item))
        month, day = key.split('_')
        print(month, day, ' '.join(val))
if not exist:
    print("None")

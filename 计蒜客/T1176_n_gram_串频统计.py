from collections import OrderedDict
num = int(input())
s = input()
d = OrderedDict()
for i in range(len(s)):
    if i + num <= len(s):
        key = s[i:i+num]
        d[key] = d.get(key, 0) + 1

sorted_values = sorted(d.values())
if sorted_values[-1] <= 1:
    print("NO")
else:
    print(sorted_values[-1])
    for key, value in d.items():
        if value == sorted_values[-1]:
            print(key)
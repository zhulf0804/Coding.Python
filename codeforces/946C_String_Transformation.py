line = input()
s = line.strip()

raw = 'abcdefghijklmnopqrstuvwxyz'
results = []
#print(raw)
#print(s)
if len(s) < 26:
    print(-1)
else:
    ind = 0
    for i in range(len(s)):
        if ind >= 26:
            results.append(s[i])
        elif ord(s[i]) <= ord(raw[ind]):
            results.append(raw[ind])
            ind += 1
        else:
            results.append(s[i])
    if ind >= 26:
        print(''.join(results))
    else:
        print(-1)
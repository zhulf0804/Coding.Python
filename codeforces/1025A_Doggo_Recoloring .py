n = int(input())
s = input()

if n == 1:
    print("Yes")
else:
    if len(set(s)) < len(s):
        print("Yes")
    else:
        print("No")
l = list(range(97, 97+26))
#for item in l:
#    print(chr(item))
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    res = [chr(l[i]) for i in range(k)] * (n // k)
    res.extend([chr(l[i]) for i in range(n % k)])
    print(''.join(map(str, res)))
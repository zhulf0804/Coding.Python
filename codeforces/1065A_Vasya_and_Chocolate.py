T = int(input())

for i in range(T):
    s, a, b, c = list(map(int, input().split()))
    ans = 0
    num1 = s // (a * c)
    num2 = s - num1 * a * c
    #print(num1, num2)
    ans += num1 * (a + b)
    ans += (num2 // c)
    print(ans)
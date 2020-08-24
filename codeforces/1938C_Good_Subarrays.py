t = int(input())
while t > 0:
    t -=1
    n, a = int(input()), input()
    ans, summ, m = 0, 0, {}
    for c in a:
        summ += (int(c) - 1)
        if summ == 0:
            ans += 1
        ans += m.get(summ, 0)
        m[summ] = m.get(summ, 0) + 1
    print(ans)
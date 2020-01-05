n = int(input())
k = int(input())
A = int(input())
B = int(input())
#print(n, k, A, B)


summ = 0
while n != 1:
    if k == 1 or n < k:
        summ += A*(n-1)
        break
    if n % k != 0:
        times = n - n // k * k
        summ += A * times
        n -= times
    else:
        t2 = A * (n - n // k)
        if B < t2:
            summ += B
        else:
            summ += t2
        n = n // k
    #print(n, summ)
print(summ)
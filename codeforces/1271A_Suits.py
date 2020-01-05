a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

max_cost = 0
if e >= f:
    mmin = min(a, d)
    max_cost += mmin * e
    max_cost += f * min(b, c, d-mmin)

else:
    mmin = min(b, c, d)
    max_cost += mmin * f
    max_cost += e * min(a, d - mmin)

print(max_cost)
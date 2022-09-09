def g1(x):
    gval = x - (x*x - 5*x + 6)
    return gval

def g2(x):
    gval = x + (x * x - 5 * x + 6)
    return gval

x10 = 1.95
x20 = 2.01
for k in range(1, 10):
    x11 = g1(x10)
    x10 = x11

    x21 = g2(x20)
    x20 = x21


print(x11, g1(x11))
print(x21, g2(x21))
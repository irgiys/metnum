def f(x):
    return 2.05*x**3-1.12*x**3-4.23

def bisection(a, b, e=10**-4, n=100):
    step = 1
    condition = True

    while condition:
        c = (a + b) / 2
        print('Iterasi ke-%d,\tC = %0.4f dan f(C) = %0.4f' % (step, c, f(c)))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        step = step + 1
        condition = abs(f(c)) > e and step <= n
    print('\nDitemukan, akarnya adalah: %0.4f' % c)

a = float(1)
b = float(2)

if f(a) * f(b) > 0.0:
    print('Nilai yang diberikan harus diantara akar.')
else:
    bisection(a, b)
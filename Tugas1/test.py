def f(x):
    return 4.15*x**5-2.23*x**3-6.35

def bisection(a, b):
    e = 10**-4
    steps = 1
    while (e >= 0.0001):
        c = (a+b) /2
        if (f(c)*f(a) > 0.0):
          a = c
        else:
          b = c
        e =  abs(a-b)
        steps += 1
        print('Iterasi ke-%d,\tC = %0.4f dan f(C) = %0.4f' % (steps, c, f(c)))
    return c

hasil = bisection(1,2) 
print('%0.4f' % (hasil))
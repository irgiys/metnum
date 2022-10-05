# Defining Function
def f(x):
    return 7.55*x**5-2.22*x**3-4.52

# Implementing Bisection Method
def bisection(a,b,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        c = (a + b)/2
        print('Iteration-%d, c = %0.4f and f(c) = %0.4f' % (step, c, f(c)))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        step = step + 1
        condition = abs(f(c)) > e

    print('\nAkarnya adalah %0.4f' % c)


a = float(0)
b = float(1)
e = 10**-4

a = float(a)
b = float(b)
e = float(e)


if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(a,b,e)
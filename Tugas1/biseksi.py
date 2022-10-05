def f(x):
    return 4.15*x**5-2.23*x**3-6.35

def bisection(a, b):
    print("="*45)
    eps = 10**-4
    counter = 1
    condition = True
    
    while condition:
        c = (a + b) / 2
        error = b - a

        print('Iterasi ke-%d, \tC = %0.4f dan f(C) = %0.4f' % (counter, c, f(c)))
      
        if f(a) * f(c) >= 0:
            a = c
        elif f(b) * f(c) >= 0:
            b = c

        counter += 1
        akar = error <= eps
      #   print(f"f(c) = {abs(f(c))} {akar}")
      #   condition = abs(f(c)) > eps
        print(f"akar {akar}") 
        condition = not akar 
    print("="*45)
    print('\nAkarnya adalah: %0.4f' % c, "\n")

a = float(1)
b = float(2)

if f(a) * f(b) < 0 :
    bisection(a, b)
else:
    print('Nilai a dan b bukan diantara akar.')
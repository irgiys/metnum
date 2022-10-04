f = lambda  x : 4.15*x**5-2.23*x**3-6.35

def bisection(a,b):
   eps = 10**-4
   steps = 1
   condition = True
   while(condition):
      c = (a+b) / 2
      if(f(a)*f(c) < 0):
         b = c
      else :
         a = c
      print('Iterasi ke-%d,\tC = %0.4f dan f(C) = %0.4f' % (steps, c, f(c)))
      

a = float(1)
b = float(2)
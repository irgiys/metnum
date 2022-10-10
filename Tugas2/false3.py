def f(x):
   return 4.15*x**5-2.23*x**3-6.35


def falsi_method(a,b,n = 10):
   i = 0
   tol = 10**-4
   c = (a*f(b) - b * f(a)) / (f(b) - f(a))
   print("%-20s %-20s %-20s %-20s %-20s" % ("i", "a", "b", "x", "f(x)/toleransi"))
   while True:
      c = (a*f(b) - b * f(a)) / (f(b) - f(a))
      error  = abs(f(c))
      print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, a, b, c, f(c)))
      if (f(a)*f(c)) < 0:
         b = c
      else:
         a = c
      i += 1
      if error < tol:
         print(f"\nNilai x didapatkan pada saat iterasi ke {i-1}, dengan nilai x = {c}")
         break

falsi_method(1,2)
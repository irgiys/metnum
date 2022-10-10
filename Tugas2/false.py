def fp_method(func, a,b,tol):
   def f(x):
      f = eval(func)
      return f
   i = 0
   c_before = 0
   c = (a*f(b) - b * f(a)) / (f(b) - f(a))
   error = abs(c - c_before)

   print("i \t a \t\t b \t\t c \t\t f(a) \t\t f(b) \t\t error")
   while error > tol:
      c_after = (a*f(b) - b * f(a)) / (f(b) - f(a))
      print("%d \t %0.4f \t %0.4f \t %0.4f \t %0.4f \t %0.4f \t %0.4f" % (i+1,a,b,c_after,f(a), f(b), error))
      if f(a) * f(b) >= 0:
         print("No root or multiple roots present")
         quit()
      elif f(c_after) * f(a) < 0:
         error = abs(c_after - b)
         b = c_after
         i = i + 1
      elif f(c_after) * f(b) < 0:
         error = abs(c_after - a)
         a = c_after
         i = i + 1
      else:
         print("Something else went wrong")
         quit()
   print(f"The error remaining is {error}, after {i} iteration")
   print(f"The root can be approximately found at {c_after}")
   print(f"The lower root boundry, a, is {a} and the upper root boundry, b, is {b}")

fp_method("4.15*x**5-2.23*x**3-6.35", 1,2,0.0001)
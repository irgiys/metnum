def f(x):
   return 4.15*x**5-2.23*x**3-6.35

a = float(1)
b = float(2)
e = 10**-4
N = 45

y1 = f(a)
y2 = f(b)

if y1 * y2 > 0:
   print("Tidak ada akar")
else:
   print("\n \tIt \ta \txr \tb \t\tf(a) \t\tf(b) \t\tError")
   it = 0
   while True:
      it = it + 1
      xr = ((f(b)*a) - (f(a)*b)) / (f(b) - f(a))
      y3 = f(xr)
      print("\n \t%d \t%0.4f \t%0.4f \t%0.4f \t\t%0.4f \t%0.4f \t%0.4f" % (it,a,xr,b,f(a), f(b), abs(xr)))
      if f(xr) * f(a) < 0:
         b = xr
         y2 = y3
      else :
         a = xr
         y1 = y3
      if it >= N and abs(f(xr) <= e):
         break
   if it <= N:
      print("Penyelesaian persamaan yang didapatkan adalah x = %0.4f dengan toleransi error %0.4f" % (xr, abs(f(xr))))
   else:
      print("Penyelesaian tidak ditemukan")

"""
   IRGIYANSYAH
   211351068
   Persamaan = 4.15x^5-2.23x^3-6.35
"""
def f(x):
    return 4.15*x**5-2.23*x**3-6.35

def regulaFalsi(a, b , toleransi, n):
    i = 0

    print("-"*68)
    print("%-9s %-9s %-9s %-9s %-9s %-9s %-9s" % ("i", "a", "b", "c","f(a)","f(b)", "f(c)"))
    print("-"*68, "\n") 
    while True:
        c = ((f(b)*a) - (f(a)*b)) / (f(b) - f(a))
        error = abs(f(c)) 
        i += 1
        print("%-4g %2s %-0.4f %2s %-0.4f %2s %-0.4f %2s %-0.4f %2s %-0.4f %2s %-0.4f\n" % (i,"" ,a, "", b, "", c,"", f(a),"",f(b),"", f(c)))
        # Syarat metode tertutup, pada kasus ini Regula Falsi
        if f(a)*f(c) < 0 : b = c
        if f(b)*f(c) < 0 : a = c
       # Jika error <= toleransi atau iterasi lebih dari sama dengan n program akan berhenti. Artinya nilai toleransi/error telah dicapai.
        if error <= toleransi or i >= n: break
    
    print("-"*68) 
    print("\nNilai c didapatkan pada iterasi ke %d, dengan nilai c = %0.4f dengan errror %0.4f" % (i,c,error))

a = float(input("Inputkan nilai atas  (a) = "))
b = float(input("Inputkan nilai bawah (b) = "))
e = float(input("Inputkan nilai toleransi = "))
n = float(input("Inputkan batas iterasi   = "))

if f(a) * f(b) < 0: regulaFalsi(a, b, e, n)
else : print('Nilai a dan b tidak diantara akar.')
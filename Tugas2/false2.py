import math

def f(x):
   # 4.15*x**5-2.23*x**3-6.35
    return 4.15*x**5-2.23*x**3-6.35

def regulaFalsi(a, b , toleransi, n):
    i = 0
    fa = f(a)   

    print("-"*55)
    print("%-9s %-9s %-9s %-9s %-9s" % ("i", "a", "b", "x", "f(c)"))
    print("-"*55) 

    # Dilakukan iterasi sampai dengan n yang diinginkan
    while(i <= n):
        c = (a*f(b)-b*f(a))/(f(b) - f(a))
        fc = f(c)
        i += 1
        error = abs(f(c))
        # Jika f(c) = 0 atau akar telah ditemukan program akan berhenti.
        # Jika |f(c)| < angka toleransi program akan berhenti. Artinya nilai toleransi/error telah dicapai.
        if (f(c) == 0 or abs(f(c)) < toleransi):
            print("-"*55) 
            print(f"\nNilai c didapatkan pada iterasi ke {i-1}, dengan nilai c = {c} dengan errror {error}")
            break
        # Jika tidak maka iterasi akan terus berjalan sampai keadaan di atas.
        else:
             print("%-4g %2s %-0.4f %2s %-0.4f %2s %-0.4f %2s %-0.4f\n" % (i,"" ,a, "", b, "", c,"", f(c)))
        
        # Syarat metode tertutup, pada kasus ini Regula Falsi
        if (fa*fc < 0):
            a = c
        else:
            b = c
    return

regulaFalsi(1, 2, 0.0001, 10)
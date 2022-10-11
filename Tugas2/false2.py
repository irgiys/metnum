def f(x):
   # 4.15*x**5-2.23*x**3-6.35
    return 4.15*x**5-2.23*x**3-6.35

def regulaFalsi(a, b , toleransi, n):
    i = 0

    print("-"*55)
    print("%-9s %-9s %-9s %-9s %-9s" % ("i", "a", "b", "c", "f(c)"))
    print("-"*55) 
    # Dilakukan iterasi sampai dengan n yang diinginkan
    while(i <= n):
        c = ((f(b)*a) - (f(a)*b)) / (f(b) - f(a))
        i += 1
        error = abs(f(c))
        # Jika f(c) = 0 atau akar telah ditemukan program akan berhenti.
        # Jika |f(c)| < angka toleransi program akan berhenti. Artinya nilai toleransi/error telah dicapai.
        if (abs(f(c)) <= toleransi):
            print("-"*55) 
            print("\nNilai c didapatkan pada iterasi ke %d, dengan nilai c = %0.4f dengan errror %0.4f" % (i,c,error))
            break
        # Jika tidak maka iterasi akan terus berjalan sampai keadaan di atas.
        else:
             print("%-4g %2s %-0.4f %2s %-0.4f %2s %-0.4f %2s %-0.4f\n" % (i,"" ,a, "", b, "", c,"", f(c)))
        # Syarat metode tertutup, pada kasus ini Regula Falsi
        if (f(a)*f(c) < 0):
            b = c
        else:
            a = c

a = float(input("Inputkan nilai atas  (a) = "))
b = float(input("Inputkan nilai bawah (b) = "))
e = float(input("Inputkan nilai toleransi = "))
n = float(input("Inputkan batas iterasi   = "))

regulaFalsi(a, b, e, n)

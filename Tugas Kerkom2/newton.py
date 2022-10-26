import timeit
# Newton Rapson
f_rill = lambda x : 4.15*x**5 - 2.53*x**3 - 6.35
f_turun = lambda x : 20.75*x**4 - 7.59*x**2

def newtonRaph(x,e = 0.000001):
    start = timeit.default_timer()
    i = 0
    xk = x
    print("\n%-1s | %-10s | %-15s | %-12s  | %-10s" % ("i", "xk", "f(x)", "f`(x)", "Em"))
    xk1 = xk
    em = 0
    while True :
        fx = f_rill(xk1)
        faks = f_turun(xk1)
        print("%-1s | %-0.4f %3s | %-0.4f %1s | %-0.4f \t | %-0.4f" %(i,xk1,"", fx,"\t", faks ,em))
        xk = xk1
        xk1 = xk  - (fx / faks)

        em = abs(xk1 - xk)
        i += 1
        if(i > 10 or em < e) : break;
    stop = timeit.default_timer()
    print('\nWaktu Eksekusi Newton: ', stop - start, "\n")  


x = float(input("Inputkan nilai x0 = "))
# e = float(input("Inputkan nilai toleran = "))
newtonRaph(x)
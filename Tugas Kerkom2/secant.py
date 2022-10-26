import timeit
# Secant
f = lambda x : (4.15*(x**5)) - (2.53*(x**3)) - 6.35

def secant(x0, x1 , e=0.00001):
    xbef = x0
    xaft = x1
    fbef = f(xbef)
    faft = f(xaft)
    em = 0
    i = 0
    print("\n%2s | %2s \t | %2s \t | %2s" % ("i", "x", "f(x)", "Em"))
    while True :
        start = timeit.default_timer()
        print("%2s | %-0.4f \t | %-0.4f \t | %-0.4f" % (i, xbef, fbef, em))
        em = abs(xaft - xbef)
        xtemp = xaft

        xaft = xaft-(faft)*(xbef-xaft)/(fbef-faft)
        xbef = xtemp
        fbef = f(xbef)
        faft = f(xaft)
        i += 1
        if(i > 10 or em < e ): break;
    stop = timeit.default_timer()
    print('\nWaktu Eksekusi Secant: ', stop - start, "\n")
satu = float(input("Input kan nilai kesatu\t= "))
dua = float(input("Input kan nilai kedua\t= "))
secant(satu,dua)
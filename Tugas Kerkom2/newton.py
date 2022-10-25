f_rill = lambda x : (2*(x**3)) - (3*(x**2)) + (1*x) - 5
f_turun = lambda x : (6*(x**2)) - (6*x) + 1

def newtonRaph(x,e = 0.00001):
    i = 0
    x0 = x
    print("%-10s %-8s\t %-10s %-10s" % ("xk", "fx", "f`x", "Em"))
    xk1 = x0
    em = 0
    while True :
        fx = f_rill(xk1)
        faks = f_turun(xk1)
        print("%-0.4f %2s  %-0.4f %2s %-0.4f %2s %-0.4f" %(xk1,"", fx,"\t", faks, "" ,em))
        x0 = xk1
        xk1 = xk1  - (fx / faks)

        em = abs(xk1 - x0)
        i += 1
        if(i > 6 or em < e) : break;


x = float(input("Inputkan nilai x0 = "))
# e = float(input("Inputkan nilai toleran = "))
newtonRaph(x)
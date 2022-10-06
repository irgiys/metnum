"""
   Definisi fungsi f(x) untuk melakukan perhitungan variabel/parameter x
   dari persamaan 4,15*x^5-2,23*x^3-6,35
"""
def f(x):
    return 4.15*x**5-2.23*x**3-6.35

"""
   Definisi fungsi biseksi untuk mencari akar dari nilai parameter a dan b
"""
def bisection(a, b):
    print("="*45)
    # Inisialisasi toleransi untuk akar yang akan dicari yaitu 10^-4 atau 0.0001
    toleran = 10**-4
    # Variable opsional untuk mengetahui berapakali iterasi dilakukan
    iteration = 1

   #  Ketika condition True jalankan iterasi
    while True:
        # Inialisasi variable c untuk mencari nilai tengah antara a dan b
        c = (a + b) / 2
        """
            Tampilkan output
            %d yaitu placeholder untuk desimal ataupun integer, yang mengarah pada variable iteration
            %0.4f yaitu placeholder dan formatting agar menerapkan 4 angka dibelakang koma untuk variable c dan f(c)
        """
        print('Iterasi ke-%d, \tC = %0.4f dan f(C) = %0.4f' % (iteration, c, f(c)))
        #  Jika f(a) dikali f(c) kurang dari 0 maka nilai b diganti dengan c
        if f(a) * f(c) < 0:
            b = c
        #  Jika f(b) dikali f(c) kurang dari 0 maka nilai a diganti dengan c
        if f(b) * f(c) < 0:
            a = c
        #  Nilai variable iteration naik +1 ketika iterasi dilakukan
        iteration += 1
        #  Jika f(c) kurang dari sama dengan toleransi iterasi selesai
        #  Fungsi abs adalah fungsi yang akan mengembalikan nilai absolute dari sebuah number
        if abs(f(c)) <= toleran :
         break
      
    print("="*45)
    #  Tampilkan output akar
    print('\nAkarnya adalah: %0.4f' % c, "\n")

"""
   Inisialisasi variable a untuk batas atas dan b untuk batas bawah 
""" 
a = float(1)
b = float(2)

#  Jika fungsi a dikali fungsi b kurang dari 0 maka jalankan fungsi biseksi diatas
if f(a) * f(b) < 0 :
    bisection(a, b)
else:
#  Selain itu artinya nilai a dan b tidak diantara akar
    print('Nilai a dan b tidak diantara akar.')
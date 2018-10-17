#persegi
def luasp(a):
        return a*a
def kelp(a):
    return a*4
#persegi panjang
def luaspp(a, b):
        return a*b
def kelpp(a, b):
    return a*
#segitiga
def luaseg(a, b):
        return a*b/2
#persegi
def kelp(a):
        return a*4
#persegi panjang
def kelpp(a, b):
        return 2*(a+b)
#segitiga
def kelseg(a, b):
        return a*b
#operasi

print("Menghitung Luas")
print("===============================")
print("Pilih Bangun Datar:")
print("1.Persegi")
print("2.Persegi Panjang")
print("3.Segitiga")
#input&output
pilihan = input("Masukan Pilihan Anda[1/2/3]: ")
#operasi
if pilihan == '1':
        l1 = int(input("Masukan Panjang Sisi: "))
        print("Luas Persegi : ", luasp(l1))
elif pilihan == '2':
        p2 = int(input("Masukan Panjang : "))
        l2 = int(input("Masukan Lebar : "))
        print("Luas Persegi Panjang : ", luaspp(p2,l2))
elif pilihan == '3':
        a = int(input("Masukan Alas : "))
        t = int(input("Masukan Tinggi : "))
        print("Luas Segitiga : ", luaseg(a,t))
else:
        print("Input Salah")





        
        




        

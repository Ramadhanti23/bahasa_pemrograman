#Jawaban1

#Hasil Print dari (Saya Belajar Bahasa Pemograman Menggunakan Python)

print("Saya Belajar Bahasa Pemograman Menggunakan Python")


#Jawaban2

#Luas Segitiga 

print(" Menghitung Luas Segitiga ")

a = float(input(" Masukan Alas : "))
b = float(input(" Masukan Tinggi : "))

luas = 0.5*a*b

print(" Hasil luas segitiga : ", luas)

#Jawaban3

class biodata :
    
    print("============================")
    print("        PROGRAM QUIZ        ")
    print("============================")
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        
    nama = input("Masukan Nama : ")
    nim = int(input("Masukan Nim : "))
    
    print("============================")
    print("        PROGRAM QUIZ        ")
    print("============================")
    print("Nama : ", nama)
    print("Nim : ", nim)
    

#Jawaban4

Nested Looping:

ListKota = ['Kalimantan', 'Sumatra', 'Sulawesi']
ListTempat = ['West', 'North', 'South']
for Kota in ListKota:
    for Tempat in ListTempat:
        print(Kota, Tempat)

#Jawaban5

def menu():
    a = "Capucino"
    b = "Teh"
    print("Pilihan")
    print("1", a)
    print("2", b)
    print("3 Exit")
    
def Capucino():
    capcin = "Pilih Capucino"
    print(capcin)
    Capucino = int(input("Masukan Harga : "))
    ppn = 10/100
    total = Capucino*ppn
    print(total) 
    hasil = Capucino+total
    print("Jumlah yang harus dibayarkan", hasil)
    
def Teh():
    teh = "Pilih Teh"
    print(teh)
    teh = int(input("Masukan Harga : "))
    ppn = 10/100
    total = teh*ppn
    print(total)
    hasil = teh+total
    print("Jumlah yang harus dibayarkan", hasil)

def data():
    nim = 20210801204
    nama = "RAMADHANTI ELVINA PRAGISYA"
    print("NIM : ", nim)
    print("NAMA : ", nama)
    
while True:
    data()
    menu()
    pil = int(input("Masukan Pilihan : "))
    if pil == 1:
        Capucino()
    elif pil == 2:
        Teh()
    elif pil == 3:
        break
    else:
        print("Pilihan anda salah")


































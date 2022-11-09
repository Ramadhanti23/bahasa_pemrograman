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
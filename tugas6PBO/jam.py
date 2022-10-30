#Nama : Ramadhanti Elvina P
#Nim : 20210801204


class Waktu :
    
    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self. detik = detik
        
    def tampil():
        jam = int(input("Masukan Jam : "))
        menit = int(input("Masukan Menit : "))
        detik = int(input("Masukan Detik : "))
        
        if jam <= 24 and menit <= 59 and detik <= 59:
            print(jam,":", menit,":", detik)
        else:
            print("format anda salah") 
    
    tampil()
        
class Waktu :
    
    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self. detik = detik
        
    def tampil():
        jam = int(input("Masukan Jam : "))
        menit = int(input("Masukan Menit :"))
        detik = int(input("Masukan Detik :"))
        
        if jam <= 24 and menit <= 60 and detik <= 60:
            print(jam,":", menit,":", detik)
        else:
            print("format anda salah") 
    
    tampil()
        
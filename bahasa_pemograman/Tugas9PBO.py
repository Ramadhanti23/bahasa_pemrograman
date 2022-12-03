class Tumbuhan :
    def __init__(self, anggrek, mawar, melati):
        self.mawar = mawar
        self.anggrek = anggrek
        self.melati = melati 
    def display(self):
        print(self.anggrek, ":", self.mawar, ":", self.melati)

class plant :
    def __init__(self):
        Tumbuhan.__init(self)
        self.tumbuh = 0
        self.jumlah_air = 0
        self.jumlah_pupuk = 0
    
    def air(self,st):
        self.jumlah_air = st.jumlah_air + 1
        
    def pupuk(self,st):
        self.jumlah_pupuk = st.jumlah_pupuk + 1
        
    def status(self,st):
        self.tumbuh = st.tumbuh + 1
        
    def jenis_plant(self, jenis):
        self.jenis = jenis 
        
def menu():
    a = "Anggrek"
    b = "Mawar"
    c = "Melati"
    print(" Silahkan Pilih Plant ")
    print("1", a)
    print("2", b)
    print("3", c)
    print("4 Exit")
    
def Anggrek():
    anggrek = " Anggrek "
    print(anggrek)
    Status = input(" Status tumbuh : Benih ")
    Air = int(input("Masukan Jumlah Air : "))
    Pupuk = int(input("Masukan Jumlah Pupuk : "))
    if Air >= 0 and Pupuk >= 3:
        print( " Plant Berhasil ")
    else:
        print(" Plant Tidak berhasil ")
    Status = input(" Status tumbuh : Tunas ")
    Air = int(input("Masukan Jumlah Air : "))
    Pupuk = int(input("Masukan Jumlah Pupuk : "))
    if Air >= 0 and Pupuk >= 3:
        print( " Plant Berhasil ")
    else:
        print(" Plant Tidak berhasil ")
    Status = input(" Status tumbuh : Tanaman Kecil ")
    Air = int(input("Masukan Jumlah Air : "))
    Pupuk = int(input("Masukan Jumlah Pupuk : "))
    if Air >= 0 and Pupuk >= 3:
        print( " Plant Berhasil ")
    else:
        print(" Plant Tidak berhasil ")
    Status = input(" Status tumbuh : Tanaman Dewasa ")
    Air = int(input("Masukan Jumlah Air : "))
    Pupuk = int(input("Masukan Jumlah Pupuk : "))
    if Air >= 0 and Pupuk >= 3:
        print( " Plant Berhasil ")
    else:
        print(" Plant Tidak berhasil ")
        

def Mawar(): 
    mawar = " Mawar "
    print(mawar)
    status = input(" Status tumbuh : Benih ")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >= 1:
        print(" Behasil Tumbuh ")
    else:
        print(" Tidak Behasil Tumbuh ")
    status = input(" Status tumbuh : Tunas")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >= 1:
        print(" Berhasil Tumbuh ")
    else:
        print(" Tidak Berhasil Tumbuh ")
    status = input(" Status tumbuh : Tanaman kecil ")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >= 1 :
        print(" Berhasil Tumbuh ")
    else:
        print(" Tidak Berhasil Tumbuh ")
    status = input(" Status tumbuh : Tanaman Dewasa ")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >= 2 :
        print(" Berhasil Tumbuh ")
    else:
        print(" Tidak Berhasil Tumbuh ")    

def Melati():
    Melati = " Melati "
    print(Melati)
    status = input(" Status tumbuh : Benih ")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >=2 :
        print(" Berhasil Tumbuh ")
    else:
        print(" Tidak Berhasil Tumbuh ")
    status = input(" Status tumbuh : Tunas ")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >=2 :
        print(" Berhasil Tumbuh ")
    else:
        print(" Tidak Berhasil Tumbuh ")
    status = input(" Status tumbuh : Tanaman kecil ")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >= 4 :
        print(" Berhasil Tumbuh ")
    else:
        print(" Tidak Berhasil Tumbuh ")
    status = input(" Status tumbuh : Tanaman Dewasa ")
    Air = int(input(" Masukan Jumlah Air : "))
    Pupuk = int(input(" Masukan Jumlah Pupuk : "))
    if Air >=0 and Pupuk >= 3 :
        print(" Berhasil Tumbuh ")
    else:
        print(" Tidak Berhasil Tumbuh ")
    
while True:
    menu()
    pil = int(input("Masukan Pilihan : "))
    if pil == 1:
        Anggrek()
    elif pil == 2:
        Mawar()
    elif pil == 3:
        Melati()
    elif pil == 4:
        break
    else:
        print("Pilihan anda salah")
    
        
    
        
    

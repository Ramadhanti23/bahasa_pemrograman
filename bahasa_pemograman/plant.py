class plant(object):
    def __init__(self, jumlah_Air, jumlah_Pupuk, Status_tumbuh):
        self.jumlah_Air = jumlah_Air
        self.jumlah_Pupuk = jumlah_Pupuk
        self.Status_tumbuh = Status_tumbuh
        
    def tumbuh(self):
        if self.Status_tumbuh < 4:
            self.jumlah_Air -= 3
            self.jumlah_Pupuk -= 1
            self.Status_tumbuh +=1
            
    def cek_kondisi_tumbuh(self):
        if self.jumlah_Air >=3 and self.jumlah_Pupuk >=1 :
            plant.cek_kondisi_tumbuh()
            
    def Beri_Air(self):
        self.jumlah_Air += 1
        plant.cek_kondisi_tumbuh()
    
    def Beri_Pupuk(self):
        self.jumlah_Pupuk += 1
        plant.cek_kondisi_tumbuh()
        
    def getstatustumbuhText(self):
        if self.Status_tumbuh == 0:
            print("Benih")
        elif self.Status_tumbuh == 1:
            print("Tunas")
        elif self.Status_tumbuh == 2:
            print("Tanaman Kecil")
        elif self.Status_tumbuh == 3:
            print("Tanaman Dewasa")
        else:
            print("berbunga")
            
    def DisplyPlant(self):
        #print(plany.getStatusTumbuhText)
        print("\njumlah_Air : {} \njumlah_Pupuk \t: {}". format(self.jumlah_Air, self.jumlah_Pupuk))
        
    def getjumlah_Air(self):
        return self.jumlah_Air
    
    def setJumlahAir(self,n):
        self.jumlah_Air= n
        
    def getjumlah_Pupuk(self):
        return self.jumlah_Pupuk
        
    def setJumlahPupuk(self, n):
        self.jumlah_Pupuk = n
        
    def getStatus_tumbuh(self):
        return self.Status_tumbuh
    
    def Statustumbuh(self, n):
        self.Status_tumbuh = n
        
#child class
 
class Anggrek(plant):
    def __init__(self, jumlah_Air, jumlah_Pupuk, Status_tumbuh, jenis):
        self.jenis = jenis
        plant.__init__(self, jumlah_Air, jumlah_Pupuk, Status_tumbuh)
        
    def anggrektumbuh(self):
        if self.Status_tumbuh < 4:
            self.jumlah_Air -= 3
            self.jumlah_Pupuk -= 1
            self.Status_tumbuh += 1
            
    def cek_kondisitumbuh(self):
        if self.jumlah_Air >= 3 and self.jumlah_Pupuk >=2:
            Anggrek.anggrektumbuh()
            
    def getjenis(self):
        return self.jenis
    
class Mawar(plant):
    def __init__(self, jumlah_Air, jumlah_Pupuk, Status_tumbuh, jenis):
        self.jenis = jenis
        plant.__init__(self, jumlah_Air, jumlah_Pupuk, Status_tumbuh)
        
    def mawartumbuh(self):
        if self.Status_tumbuh < 8:
            self.jumlah_Air -= 6
            self.jumlah_Pupuk -= 3
            self.Status_tumbuh += 3
            
    def cek_kondisitumbuh(self):
        if self.jumlah_Air >= 3 and self.jumlah_Pupuk >=2:
            Mawar.mawartumbuh()
            
    def getjenis(self):
        return self.jenis

class Melati(plant):
    def __init__(self, jumlah_Air, jumlah_Pupuk, Status_tumbuh, jenis):
        self.jenis = jenis
        plant.__init__(self, jumlah_Air, jumlah_Pupuk, Status_tumbuh)
        
    def melatitumbuh(self):
        if self.Status_tumbuh < 4:
            self.jumlah_Air -= 3
            self.jumlah_Pupuk -= 1
            self.Status_tumbuh += 1
            
    def cek_kondisitumbuh(self):
        if self.jumlah_Air >= 3 and self.jumlah_Pupuk >=2:
            Melati.melatitumbuh()
            
    def getjenis(self):
        return self.jenis


Tanaman1 = Anggrek(2, 3, 4, 'Anggrek')
print("Jenis Tanaman \t: {}".format(Tanaman1.jenis))
Tanaman1.getstatustumbuhText()
Tanaman1.DisplyPlant()

Tanaman2 = Mawar(1, 4, 2, 'Mawar')
print("Jenis Tanaman \t: {}".format(Tanaman2.jenis))
Tanaman2.getstatustumbuhText()
Tanaman2.DisplyPlant()

Tanaman3 = Melati(3, 1, 1, 'Melati')
print("Jenis Tanaman \t: {}".format(Tanaman3.jenis))
Tanaman3.getstatustumbuhText()
Tanaman3.DisplyPlant()
    
        
      
        
    
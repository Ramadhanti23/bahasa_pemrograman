class plant(object):
    
    def __init__(self, jumlah_air, jumlah_pupuk, status_tumbuh):
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk
        self.status_tumbuh = status_tumbuh
        
    def Tumbuh(self):
        if self.status_tumbuh < 4:
            self.jumlah_air -= 3
            self.jumlah_pupuk -= 1
            self.status_tumbuh += 1
            
    def cek_kondisi_tumbuh(self):
        if self.jumlah_air >= 3 and self.jumlah_pupuk >= 1:
            plant.Tumbuh()
            
    def beri_air(self):
        self.jumlah_air += 1
        plant.cek_kondisi_tumbuh()
        
    def beri_pupuk(self):
        self.jumlah_pupuk += 1
        plant.cek_kondisi_tumbuh()
        
    def getstatustumbuhText(self):
        if self.status_tumbuh == 0:
            print("Benih")
        elif self.status_tumbuh == 1:
            print("Tunas")
        elif self.status_tumbuh == 2:
            print("Tanaman kecil") 
        elif self.status_tumbuh == 3:
            print("Tanaman Dewasa")
        else:
            print("berbunga")
            
    def Displyplant(self):
        print("Beri_air \t: {} \nBeri_pupuk \t: {}". format(self.jumlah_air, self.jumlah_pupuk))
        
    def getjumlah_air(self):
        return self.jumlah_air 
    
    def setjumlahair(self, n):
        self.jumlah_air= n
    
    def getjumlah_pupuk(self):
        return self.jumlah_pupuk    
    
    def setjumlahpupuk(Self, n):
        Self.jumlah_pupuk = n
        
    def getstatus_tumbuh(self):
        return self.status_tumbuh
    
    def setstatustumbuh(self , n):
        self.status_tumbuh = n
        
class Anggrek(plant):
    def __init__(self, jumlah_air, jumlah_pupuk, status_tumbuh, jenis):
        self.jenis = jenis 
        plant.__init__(self, jumlah_air, jumlah_pupuk, status_tumbuh)
    
    def anggrektumbuh(self):
        if self.status_tumbuh < 4:
            self.jumlah_air-= 3
            self.jumlah_pupuk -= 1 
            self.status_tumbuh += 1
    
    def cek_kondisi_tumbuh(self):
        if self.jumlah_air >= 3 and self.jumlah_pupuk >=2:    
            Anggrek.anggrektumbuh()
            
    def getjenis(self):
        return self.jenis
    
class Mawar(plant):
    def __init__(self, jumlah_air,jumlah_pupuk, status_tumbuh, jenis):
        self.jenis = jenis
        plant.__init__(self, jumlah_air, jumlah_pupuk, status_tumbuh)
        
    def mawartumbuh(self):
        if self.status_tumbuh < 8:
            self.jumlah_air -= 6
            self.jumlah_pupuk -= 3
            self.status_tumbuh += 3
    
    def cek_kondisi_tumbuh(self):
        if self.jumlah_air >= 3 and self.jumlah_pupuk >=2:
            Mawar.mawartumbuh()
    
    def getjenis(self):
        return self.jenis
    
class Melati(plant):
    def __init__(self, jumlah_air, jumlah_pupuk, status_tumbuh, jenis):
        self.jenis = jenis
        plant.__init__(self, jumlah_air, jumlah_pupuk, status_tumbuh)
        
    def melatitumbuh(self):
        if self.status_tumbuh < 4 :
            self.jumlah_air -= 3
            self.jumlah_pupuk -= 1
            self.status_tumbuh  += 1
    def cek_kondisi_tumbuh(self):
        if self.jumlah_air >= 3 and self.jumlah_pupuk >=2:
            Melati.melatitumbuh()
            
    def getjenis(self):
        return self.jenis
    
tanaman1 = Anggrek( 0, 0, 0, 'Anggrek')
tanaman1.getstatustumbuhText()
print("Jenis tanaman \t: {}". format(tanaman1.jenis))
tanaman1.Displyplant()

tanaman2 = Anggrek( 1, 1, 1, 'Anggrek')
tanaman2.getstatustumbuhText()
print("Jenis tanaman \t: {}". format(tanaman2.jenis))
tanaman2.Displyplant()

tanaman3 = Anggrek( 3, 2, 3, 'Anggrek')
tanaman3.getstatustumbuhText()
print("Jenis tanaman \t{}". format(tanaman3.jenis))
tanaman3.Displyplant()

tanaman4 = Anggrek( 2, 2, 3, 'Anggrek')
tanaman4.getstatustumbuhText()
print("Jenis tanaman \t{}". format(tanaman4.jenis))
tanaman4.Displyplant()

tanaman5 = Mawar( 0, 0, 0, 'Mawar')
tanaman5.getstatustumbuhText()
print("Jenis tanaman \t{}".format(tanaman5.jenis))
tanaman5.Displyplant()

tanaman6 = Mawar( 1, 1, 1, 'Mawar')
tanaman6.getstatustumbuhText()
print("Jenis tanaman \t{}".format(tanaman6.jenis))
tanaman6.Displyplant()

tanaman5 = Mawar( 2, 1, 2, 'Mawar')
tanaman5.getstatustumbuhText()
print("Jenis tanaman \t{}".format(tanaman5.jenis))
tanaman5.Displyplant()

tanaman8 = Mawar( 2, 3, 3, 'Mawar')
tanaman8.getstatustumbuhText()
print("Jenis tanaman \t{}".format(tanaman8.jenis))
tanaman8.Displyplant()

tanaman9 = Melati( 0, 1, 0, 'Melati')
tanaman9.getstatustumbuhText()
print("Jenis tanaman \t:{}".format(tanaman9.jenis))
tanaman9.Displyplant()

tanaman10 = Melati( 1, 2, 1, 'Melati')
tanaman10.getstatustumbuhText()
print("Jenis tanaman \t:{}".format(tanaman10.jenis))
tanaman10.Displyplant()

tanaman11 = Melati( 2, 3, 2, 'Melati')
tanaman11.getstatustumbuhText()
print("Jenis tanaman \t:{}".format(tanaman11.jenis))
tanaman11.Displyplant()

tanaman12 = Melati( 5, 4, 3, 'Melati')
tanaman12.getstatustumbuhText()
print("Jenis tanaman \t:{}".format(tanaman12.jenis))
tanaman12.Displyplant()

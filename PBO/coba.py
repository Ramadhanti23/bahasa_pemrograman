import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="gray")
window.geometry("450x500")

class plant:
    frm =ttk.Frame(window,padding="10")
    frm.pack(padx=60,pady=40,fil="x",expand=True)

    def __init__(self):
        self.jumlah_air = 0
        self.jumlah_pupuk = 0
        self.status_tumbuh = 0 
        self.status_tumbuh = "Benih"
    
    def getjumlah_air(self):
        return self.jumlah_air 
    
    def getjumlah_pupuk(self):
        return self.jumlah_pupuk    
        
    def getstatus_tumbuh(self):
        return self.status_tumbuh
    
    def setStatusBerbunga(self):
        self.statusTumbuh = "Berbunga"
        
    def tampil(self):
        print("Status Tanaman : {}\nBeri Air : {}/3 \nBeri Pupuk : {}/1".format(self.status_tumbuh,self.jumlah_air,self.jumlah_pupuk))
        
        
    def Tumbuh(self):
        if self.status_tumbuh < 4:
            self.jumlah_air -= 3
            self.jumlah_pupuk -= 1
            self.status_tumbuh += 1
            self.status_tumbuh = self.getstatustumbuhText()
            
    def cek_kondisi_tumbuh(self):
        if self.jumlah_air >= 3 and self.jumlah_pupuk >= 1:
            self.Tumbuh()
            
    def beri_air(self):
        self.jumlah_air += 1
        self.cek_kondisi_tumbuh()
        
    def beri_pupuk(self):
        self.jumlah_pupuk += 1
        self.cek_kondisi_tumbuh()
        
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
            
        
class Anggrek(plant):
    def __init__(self,  jenis):
        super().__init__()
        self.jenis = jenis 
            
    def getjenis(self):
        return self.jenis
    
class Mawar(plant):
    def __init__(self, jenis):
        super().__init__()
        self.jenis = jenis
    
    def getjenis(self):
        return self.jenis
    
class Melati(plant):
    def __init__(self, jenis):
        super().__init__()
        self.jenis = jenis
            
    def getjenis(self):
        return self.jenis
    
tanaman1 = Anggrek("Anggrek")
tanaman2 = Mawar("Mawar")
tanaman3 = Melati("Melati")

def data(lihatShow,jenis,btn,info):
    if jenis.getStatusTumbuh != "Tanaman Besar" and jenis.getStatusTumbuh != "Berbunga":
        if "1.Beri Air" in btn["text"]:
            if jenis.getJumlahAir < 3:
                jenis.beriAir()
                info["text"] = ""
            else:
                info["text"] = "tanaman berhasil"

        elif "2.Beri Pupuk" in btn["text"]:
            if jenis.getJumlahPupuk < 1:
                jenis.beriPupuk()
                info["text"] = ""
            else:
                info["text"] = "Sudah cukup"
    else:
        info["text"] = f"{jenis.getJenis()} Sudah Besar! silahkan urus tanaman Lainnya"
        jenis.setStatusBerbunga

    lihatShow["text"] = f"{jenis.tampilData}"
    
    
def tumbuhan(jenis, *args):
    for i in args:
        i.destroy()
        
    frm = plant.frm
        
    judul2 = ttk.Label(frm,text=f" Eksekusi Tanaman {jenis.getjenis()} ")
    judul2.pack(padx="10",pady="10",fil="x",expand=True)
    
    lihatShow = ttk.Label(frm,text=f"{jenis.tampilData}")
    lihatShow.pack(padx="10",pady="5",fil="x",expand=True)

    info = ttk.Label(frm,text="")
    info.pack(padx="10",pady="5",fil="x",expand=True)
            
    btn_air = ttk.Button(frm,text="1.Beri Air", command=lambda : tumbuhan(lihatShow,jenis,btn_air,info))
    btn_air.pack(padx=10,pady=10,fil="x",expand=True)    
    
    btn_pupuk = ttk.Button(frm,text="2.Beri Pupuk", command=lambda : tumbuhan(lihatShow,jenis,btn_pupuk,info))
    btn_pupuk.pack(padx=10,pady=10,fil="x",expand=True)
    
    btn_exit2 = ttk.Button(frm,text="3.Exit",command=window.destroy)
    btn_exit2.pack(padx=10,pady=10,fil="x",expand=True)

# window = tk.Tk()
# window.configure(bg="gray")
# window.geometry("450x500")
 
# # print(tanaman1.jumlah_air)
def pilihan(*args):
    for i in args:
        i.destroy()
        
    frm = plant.frm
    
    judul = ttk.Label(frm,text="Pilihan")
    judul.pack(padx="10",pady="10",fil="x",expand=True)
    
    btn_a = ttk.Button(frm,text="1.Anggrek", command=lambda : [pilihan(btn_a,btn_m,btn_mel,btn_exit)])
    btn_a.pack(padx=10,pady=10,fil="x",expand=True)
    
    btn_m = ttk.Button(frm,text="2.Mawar", command=lambda : [pilihan(btn_a,btn_m,btn_mel,btn_exit)])
    btn_m.pack(padx=10,pady=10,fil="x",expand=True)
    
    btn_mel = ttk.Button(frm,text="3.Melati", command=lambda : [pilihan(btn_a,btn_m,btn_mel,btn_exit)])
    btn_mel.pack(padx=10,pady=10,fil="x",expand=True)
    
    btn_exit = ttk.Button(frm,text="4.Exit",command=window.destroy)
    btn_exit.pack(padx=10,pady=10,fil="x",expand=True)

window.mainloop()

if __name__ == "__pilihan__":
    pilihan()

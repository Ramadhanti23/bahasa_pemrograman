import tk 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class Plant:
    def __init__(self):
        self.status = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0    
        self.statusTumbuh = "Benih"
    
    @property    
    def getJumlahAir(self):
        return self.jumlahAir
    
    @property
    def getJumlahPupuk(self):
        return self.jumlahPupuk
    
    @property    
    def getStatusTumbuh(self):
        return self.statusTumbuh

    @property
    def setStatusberbunga(self):
        self.statusTumbuh = "Berbunga"
    
    @property
    def tampil(self):
        return "Status Tanaman : {}\nBeri Air : {}/3 \nBeri Pupuk:  {}/1".format(self.statusTumbuh,self.jumlahAir,self.jumlahPupuk)

    def beriAir(self):
        self.jumlahAir += 1
        self.cek_kondisi_tumbuh()
    
    def beriPupuk(self):
        self.jumlahPupuk += 1
        self.cek_kondisi_tumbuh()

    def cek_kondisi_tumbuh(self):
        if self.status < 4:
            if self.jumlahAir >= 3 and self.jumlahPupuk >= 1 :
                self.tumbuh()

    def tumbuh(self):
        self.jumlahAir -= 3
        self.jumlahPupuk -= 1
        self.status += 1
        self.statusTumbuh = self.getStatusTumbuhText()

    def getStatusTumbuhText(self):
        if self.status == 0:
           return "Benih"
        elif self.status == 1:
            return "Tunas"
        elif self.status == 2:
            return "Tanaman Kecil"
        elif self.status == 3:
            return "Tanaman Besar"
        return "Berbunga"
    
class Anggrek(Plant):
    def __init__(self,jenis_bunga):
        super().__init__()
        self.jenis = jenis_bunga

    def getJenis(self):
        return self.jenis

class Mawar(Plant):
    def __init__(self,jenis_bunga):
        super().__init__()
        self.jenis = jenis_bunga
    
    def getJenis(self):
        return self.jenis

class Melati(Plant):
    def __init__(self,jenis_bunga):
        super().__init__()
        self.jenis = jenis_bunga
  
    def getJenis(self):
        return self.jenis

bunga1 = Anggrek("Anggrek")
bunga2 = Mawar("Mawar")
bunga3 = Melati("Melati")

def data(Showinfo,jenis, messagebox):
    if jenis != "Tanaman Besar" and jenis != "Berbunga":
        if "1.Beri Air" in messagebox["text"]:
            if jenis.getJumlahAir < 3:
                jenis.beriAi
                messagebox["text"]= "Ayo input"
            else:
                messagebox["text"] = "Info : berhasil!"

        elif "2.Beri Pupuk" in messagebox["text"]:
            if jenis.getJumlahPupuk < 1:
                jenis.beriPupuk()
                messagebox["text"] = "Ayo input"
            else:
                messagebox["text"] = "Info : berhasil"
    else:
        messagebox["text"] = f"{jenis.getJenis()} Tanaman Behasil"
        jenis.setStatusberbunga

    Showinfo["text"] = f"{jenis.tampil}"


window = tk.Tk()
window.configure(bg="gray")
window.geometry("450x500")

frm =ttk.Frame(window,padding="50")
frm.pack(padx=70,pady=40,fil="x",expand=True)

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

def pilihan(*args):
    for i in args:
        i.destroy()
        
    def beri_air():
        messagebox.showinfo("Beri Air", "Beri Air berhasil")
    
        
    judul2 = ttk.Label(frm, text=f" Beri Air ")
    judul2.pack(padx="10",pady="10",fil="x",expand=True)
        
    btn_air = ttk.Button(frm, text="1.Beri Air", command=lambda )
    btn_air.pack(padx=10,pady=10,fil="x",expand=True)
      

    
    def beri_pupuk():
        messagebox.showinfo(" Beri pupuk ", "Beri Pupuk Berhasil")
    
           
    judul2 = ttk.Label(frm, text=f" Beri Pupuk  ")
    judul2.pack(padx="10",pady="10",fil="x",expand=True)

    btn_pupuk = ttk.Button(frm,text="2.Beri Pupuk", command=beri_pupuk)
    btn_pupuk.pack(padx=10,pady=10,fil="x",expand=True)

    btn_exit2 = ttk.Button(frm,text="3.Exit",command=window.destroy)
    btn_exit2.pack(padx=10,pady=10,fil="x",expand=True)
    

# window = tk.Tk()
# window.configure(bg="gray")
# window.geometry("450x500")

# print(tanaman1.jumlah_air)

# frm =ttk.Frame(window,padding="50")
# frm.pack(padx=70,pady=40,fil="x",expand=True)


btn_a = ttk.Button(frm,text="1.Anggrek",command=lambda : pilihan(btn_a,btn_m,btn_mel,btn_exit))
btn_a.pack(padx=10,pady=10,fil="x",expand=True)

btn_m = ttk.Button(frm,text="2.Mawar", command=lambda : pilihan(btn_a,btn_m,btn_mel,btn_exit))
btn_m.pack(padx=10,pady=10,fil="x",expand=True)

btn_mel = ttk.Button(frm,text="3.Melati")
btn_mel.pack(padx=10,pady=10,fil="x",expand=True)

btn_exit = ttk.Button(frm,text="4.Exit",command=window.destroy)
btn_exit.pack(padx=10,pady=10,fil="x",expand=True)

window.mainloop()

# if __name__ == "__main__":
#     main()

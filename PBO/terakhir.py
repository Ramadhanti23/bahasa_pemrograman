import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os

window = tk.Tk()
window.configure(bg="DarkSlateGrey")
window.geometry("450x500")
window.resizable(False,False)

class Plant:
    frm = ttk.Frame(window,padding="10")
    frm.pack(padx=60,fil="x",expand=True)
    
    def __init__(self):
        self.status = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0
        self.__statusTumbuh = "Benih"
    

    @property
    def getJumlahAir(self):
        return self.__jumlahAir
    @property
    def getJumlahPupuk(self):
        return self.__jumlahPupuk
    
    @property
    def getStatusTumbuh(self):
        return self.__statusTumbuh

    @property
    def setStatusBerbunga(self):
        self.__statusTumbuh = "Berbunga"

    @property
    def tampilData(self):
        return "Status Tanaman : {}\nBeri Air : {}/3 \nBeri Pupuk : {}/1".format(self.statusTumbuh,self.jumlahAir,self.jumlahPupuk)

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
            print ("Benih")
        elif self.__status == 1:
            print ("Tunas")
        elif self.__status == 2:
            print ("Tanaman Kecil")
        elif self.__status == 3:
            print ("Tanaman Besar")
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

def data(dataShow,label_tunas,jenis,btn,info):
    if jenis.getStatusTumbuh != "Tanaman Besar" and jenis.getStatusTumbuh != "Berbunga":
        if "1.Beri Air" in btn["text"]:
            if jenis.getJumlahAir < 3:
                jenis.beriAir()
                info["text"] = ""
            else:
                info["text"] = "Info : Air Sudah Cukup!"

        elif "2.Beri Pupuk" in btn["text"]:
            if jenis.getJumlahPupuk < 1:
                jenis.beriPupuk()
                info["text"] = ""
            else:
                info["text"] = "Info : Pupuk Sudah Cukup!"
    else:
        info["text"] = f"{jenis.getJenis()} Sudah Besar! silahkan urus tanaman Lainnya"
        jenis.setStatusBerbunga
        
    dataShow()

def pilihBunga(jenis,*args):  
    for i in args:
        i.destroy()
        
    frm = Plant.frm

    judul2 = ttk.Label(frm,text=f"Menu Method {jenis.getJenis()} ")
    judul2.pack(padx="10",pady="10",fil="x",expand=True)

    info = ttk.Label(frm,text="")
    info.pack(padx="10",pady="5",fil="x",expand=True)

    dataShow = ttk.Label(frm,text=f"{jenis.tampilData}")
    dataShow.pack(padx="10",pady="5",fil="x",expand=True)

    btn_beriAir = ttk.Button(frm,text="1.Beri Air",command=lambda: [data(dataShow,label_tunas,jenis,btn_beriAir,info)])
    btn_beriAir.pack(padx=10,pady=5,fil="x",expand=True)

    btn_beriPupuk = ttk.Button(frm,text="2.Beri Pupuk",command=lambda : data(dataShow,label_tunas,jenis,btn_beriPupuk,info))
    btn_beriPupuk.pack(padx=10,pady=5,fil="x",expand=True)

    btn_exit2 = ttk.Button(frm, text="3.Exit",command=lambda: [data(label_tunas,judul2,btn_beriAir,btn_beriPupuk,btn_exit2,info,dataShow)])
    btn_exit2.pack(padx=10,pady=5,fill="x",expand=True)

def main(*args):
    if args:
        for i in args:
            i.destroy()

    frm = Plant.frm

    judul = ttk.Label(frm,text="Pilih Bunga")
    judul.pack(padx="10",pady="10",fil="x",expand=True)

    btn_anggrek = ttk.Button(frm,text="1.Anggrek",command=lambda: [pilihBunga(bunga_anggrek,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_anggrek.pack(padx=10,pady=5,fil="x",expand=True)

    btn_mawar = ttk.Button(frm,text="2.Mawar",command=lambda: [pilihBunga(bunga_mawar,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_mawar.pack(padx=10,pady=5,fil="x",expand=True)

    btn_melati = ttk.Button(frm,text="3.Melati",command=lambda: [pilihBunga(bunga_melati,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_melati.pack(padx=10,pady=5,fil="x",expand=True)

    btn_exit = ttk.Button(frm, text="4.Exit",command=window.destroy)
    btn_exit.pack(padx=10,pady=5,fill="x",expand=True)

    window.mainloop()

if __name__ == "__main__":
    main()

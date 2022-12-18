import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
# from PIL import Image, ImageTk
import os

window = tk.Tk()
# window.title("Tugas PBO - Tek Kheng - 20210801205")
window.configure(bg="Grey")
window.geometry("450x500")
window.resizable(False,False)

class Plant:
    frm = ttk.Frame(window,padding="50")
    frm.pack(padx=70,fil="x",expand=True)
    
    def __init__(self):
        self.status = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0
        # self.__level = 0
        
        self.statusTumbuh = "Benih"
        # self.__imgPlant = "Benih.png"

    # @property
    # def tampilImage(self):
    #     self.src_img = Image.open(f"img/{self.getImage}").resize((50, 50), Image.ANTIALIAS)
    #     self.img_plant = ImageTk.PhotoImage(self.src_img)
    #     return self.img_plant

    # @property
    # def getImage(self):
    #     return self.__imgPlant
    
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
    def setStatusBerbunga(self):
        self.statusTumbuh = "Berbunga"
        # self.__imgPlant = "Berbunga.png"
        # self.__level = "Max"

    @property
    def tampil(self):
        return "Status Tanaman : berhasil \nBeri Air : 3 \nBeriPupuk : 1".format(self.statusTumbuh,self.jumlahAir,self.jumlahPupuk)

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
        # self.__level += 1
        self.statusTumbuh = self.getStatusTumbuhText()
        # self.__imgPlant = self.getStatusTumbuhText() + ".png"

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
    def __init__(self,jenisbunga):
        super().__init__()
        self.jenis = jenisbunga

    def getJenis(self):
        return self.jenis

class Mawar(Plant):
    def __init__(self,jenisbunga):
        super().__init__()
        self.jenis = jenisbunga
    
    def getJenis(self):
        return self.jenis

class Melati(Plant):
    def __init__(self,jenisbunga):
        super().__init__()
        self.jenis = jenisbunga
  
    def getJenis(self):
        return self.jenis

bunga_anggrek = Anggrek("Anggrek")
bunga_mawar = Mawar("Mawar")
bunga_melati = Melati("Melati")

def akhir(dataShow,jenis,btn,info):
    if jenis.getStatusTumbuh != "Tanaman Besar" and jenis.getStatusTumbuh != "Berbunga":
        if "1.Beri Air" in btn["text"]:
            if jenis.getJumlahAir < 3:
                jenis.beriAir()
                info["text"] = ""
            else:
                info["text"] = "Info : berhasil!"

        elif "2.Beri Pupuk" in btn["text"]:
            if jenis.getJumlahPupuk < 1:
                jenis.beriPupuk()
                info["text"] = ""
            else:
                info["text"] = "Info : berhasil"
    else:
        info["text"] = f"{jenis.getJenis()} Tanaman Behasil"
        jenis.setStatusBerbunga

    dataShow["text"] = f"{jenis.tampil}"
    # label_tunas["image"] = f"{jenis.tampilImage}"

def pilih(jenis,*args):  
    for i in args:
        i.destroy()
        
    frm = Plant.frm

    judul2 = ttk.Label(frm,text=f" Eksekusi Tanaman {jenis.getJenis()} ")
    judul2.pack(padx="10",pady="10",fil="x",expand=True)

    info = ttk.Label(frm,text="")
    info.pack(padx="10",pady="5",fil="x",expand=True)
    
    # label_tunas = ttk.Label(frm,image=jenis.tampilImage)
    # label_tunas.pack(padx="10",pady="5",fil="x",expand=True)

    dataShow = ttk.Label(frm,text=f"{jenis.tampil}")
    dataShow.pack(padx="10",pady="5",fil="x",expand=True)

    btn_beriAir = ttk.Button(frm,text="1.Beri Air",command=lambda: [akhir(dataShow,jenis,btn_beriAir,info)])
    btn_beriAir.pack(padx=10,pady=5,fil="x",expand=True)

    btn_beriPupuk = ttk.Button(frm,text="2.Beri Pupuk",command=lambda : akhir(dataShow,jenis,btn_beriPupuk,info))
    btn_beriPupuk.pack(padx=10,pady=5,fil="x",expand=True)
    
    # btn_exit2 = ttk.Button(frm,text="3.Exit",command=window.destroy)
    # btn_exit2.pack(padx=10,pady=10,fil="x",expand=True)

    btn_exit2 = ttk.Button(frm, text="3.Exit",command=lambda: [main(judul2,btn_beriAir,btn_beriPupuk,btn_exit2,info,dataShow)])
    btn_exit2.pack(padx=10,pady=5,fill="x",expand=True)

def main(*args):
    if args:
        for i in args:
            i.destroy()

    frm = Plant.frm

    judul = ttk.Label(frm,text="Pilih Bunga")
    judul.pack(padx="10",pady="10",fil="x",expand=True)

    btn_anggrek = ttk.Button(frm,text="1.Anggrek",command=lambda: [pilih(bunga_anggrek,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_anggrek.pack(padx=10,pady=5,fil="x",expand=True)

    btn_mawar = ttk.Button(frm,text="2.Mawar",command=lambda: [pilih(bunga_mawar,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_mawar.pack(padx=10,pady=5,fil="x",expand=True)

    btn_melati = ttk.Button(frm,text="3.Melati",command=lambda: [pilih(bunga_melati,judul,btn_anggrek,btn_mawar,btn_melati,btn_exit)])
    btn_melati.pack(padx=10,pady=5,fil="x",expand=True)

    btn_exit = ttk.Button(frm, text="4.Exit",command=window.destroy)
    btn_exit.pack(padx=10,pady=5,fill="x",expand=True)

    window.mainloop()

if __name__ == "__main__":
    main()

class product:
    
# attribute
    def __init__(self, id, nama, jumlah,harga):
# constructor
        self.id = id
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def __del__(self):
        print("delete")  

    def data(self):
        print("id product = ", self.id)
        print("nama produk = ", self.nama)
        print("jumlah product =", self.jumlah)
        print("harga product =", self.harga)

a = product("1270060600", "Album NCT 127", "1","325000")  
#print(product.__dict__)

a.data()
del a

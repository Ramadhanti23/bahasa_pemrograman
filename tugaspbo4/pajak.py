print (" Toko Baju Mak Onde ")

def total( harga_barang, pajak):
    return harga_barang - pajak

harga_barang = int(input(" Masukan harga barang = "))
potongan = int(input(" Masukan harga potongan = "))
harga_potongan = harga_barang - potongan 
total = harga_potongan * 1.0

print("harga barang kamu sekarang = ", total)

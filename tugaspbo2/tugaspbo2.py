Nama = input("Masukan Nama Anda : ")
Nim = input ("Masukan NIM Anda : ")
jenis_kelamin = input("Masukan Jenis Kelamin Anda : ")
Tanggal_input_nilai = input("Masukan Tanggal Input : ")
Mata_Kuliah = input("Masukan Mata Kuliah : ")
Absensi = float(input("Masukan nilai Absensi : "))
Tugas = float(input("Masukan Nilai Tugas : "))
UTS = float(input("Masukan Nilai UTS : "))
UAS = float(input("Masukan Nilai UAS : "))

Nilai_akhir=(Absensi*20/100) + (Tugas*20/100) + (UTS*40/100) + (UAS*40/100) 

#Hasil

print("Output")

print("Nama :" ,Nama)
print("Nim : " ,Nim)
print("jenis kelamin: ", jenis_kelamin)
print("Tanggal Input Nilai : ", Tanggal_input_nilai)
print("Masukan mata kuliah : ", Mata_Kuliah)
print("Absensi : ", Absensi)
print("Nilai Tugas : ", Tugas)
print("Nilai UTS : ", UTS)
print("Nilai UAS  : ", UAS)
print("Nilai Akhir : ", Nilai_akhir)

if Nilai_akhir >= 80 and Nilai_akhir < 100:
    print("Grade : A")
elif Nilai_akhir >= 77 and Nilai_akhir < 79.9:
    print("Grade : A-")
elif Nilai_akhir >= 74 and Nilai_akhir < 76.9: 
    print("Grade : B+") 
elif Nilai_akhir >= 71 and Nilai_akhir < 73.9:
    print("Grade : B")
elif Nilai_akhir >= 68 and Nilai_akhir < 70.9:
    print("Grade : B-")
elif Nilai_akhir >= 64 and Nilai_akhir < 67.9:
    print("Grade : C+")
elif Nilai_akhir >= 60 and Nilai_akhir < 63.9:
    print("Grade : C")
elif Nilai_akhir >= 50 and Nilai_akhir < 59:
    print("Grade : D") 
elif Nilai_akhir >= 0 and Nilai_akhir < 49:
    print("Grade : E")

if Nilai_akhir >= 63:
    print("keterangan : Lulus")
else:
    print("Keterangan : Tidak Lulus")   


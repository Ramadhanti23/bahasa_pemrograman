#Akses function 

def data ():
  nama = str(input(" Masukan nama anda: "))
  nim = str(input(" Masukan nim anda : "))
  if nama:
    print ("Hello " + str(nama))
  else:
    print("Hello World") 
  if nim:
    print ( str(nim))
  return 
  
data()


def hitung(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= hitung(4)
print(func(4))

    


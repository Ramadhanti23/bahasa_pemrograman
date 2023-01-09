#Create Class

class MyClass:
    x = " Ramadhanti Elvina Pragisya "
    y = " 20210801204 "
    print (x, y)

#class with __init__ fuction    
class Person:
  def __init__(self, matkul, tugas):
    self.matkul = matkul
    self.tugas = tugas

p1 = Person(" Bahasa Pemograman ", 13 )

print(p1.matkul)
print(p1.tugas)

    
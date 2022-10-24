#Looping python with range 
for i in range (6):
    print("Perulangan ke -", i)
    
#Looping python with break
for i in range(10, 20):
    print(i,' x ',i ,' = ',i*i)
    if (i == 15):
        break
  
  
#Looping python with continue 
for i in range(1, 10):
    if (i == 5):
        continue
    print(i,' x ',i ,' = ',i*i)

#Nested Looping
Listidentitas = ["Red", "Big", "Tasty"]
Listbuah = ["apple", "banana", "Anggur"]

for identitas in Listidentitas:
    for buah in Listbuah:
        print(identitas, buah)




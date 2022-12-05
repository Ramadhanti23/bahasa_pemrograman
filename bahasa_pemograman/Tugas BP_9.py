#Contoh Pointer 
a = 9
b = a

a = 2 
print(" a = ", a)
print(" b = ", b)

def reserveArray(array):
    awal, akhir = 0, len(array) - 1
    while awal<akhir:
        array[awal], array[akhir] = array[akhir], array[awal]
        awal +=1
        akhir -=1
        
array = [ 10, 20, 30, 40, 50, 60]
reserveArray(array)
print(array)
        
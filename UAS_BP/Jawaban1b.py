#Rekursif 

def factorial(n):
    if (n == 0):
        return 1 
    else:
        return n*factorial(n-1)
    
print(factorial (10))

def faktorial(n):
     if n <= 1:
         return 1
     else:
         return n * faktorial(n-1)
print ('====== FAKTORIAL ======')
i = 0
x = int (input("Masukkan Bilangan : "))
while i<=x :
    print (i,'! = ',faktorial(i))
    i+=1
            
#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, 
#cuál es el número máximo y cuál es el número mínimo

i = 1
mayores = 0
menores = 0
num_maximo = int()
num_minimo = int()

while i < 6:
    numero = int(input("ingrese un número: "))
    if numero >100 :
        mayores += 1
    elif numero <100 :
        menores +=1
    
    if numero >= num_maximo:
        num_maximo = numero
    else:  
        num_minimo = numero
    i +=1



print("Cantidad de números mayores a 100: ", mayores)
print("Cantidad de números menores a 100: ", menores)
print("El número máximo ingresado es: ", num_maximo)
print("El número mínimo ingresado es: ", num_minimo)




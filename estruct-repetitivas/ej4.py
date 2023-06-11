#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

i =1
num_positivo= int()
num_negativo= int()
suma_positivos= int()

while i<=10:
    print("cantidad de números ingresados :", i)
    numero = int(input("Ingrese un número entero :"))
    if numero > 0:
        num_positivo +=1
        suma_positivos = suma_positivos + numero
    else:
        num_negativo +=1

    i +=1
print("La cantidad de números positivos ingresados son: ", num_positivo, " y su sumatoria es :", suma_positivos)
    


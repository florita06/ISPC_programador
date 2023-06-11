#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

i = 1
while i <=15:
    n = int(input("Ingrese un número negativo"))
    resultado= abs(n)
    print("El numero ingresado es", n , "el número positivo es: ", resultado)
    i+=1
    print("El programa ha finalizado")

    


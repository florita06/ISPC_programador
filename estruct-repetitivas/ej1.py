#Realice un programa que lea 4 números y diga cuántos son pares y
#cuantos impares y devuelva la sumatoria de los pares
i= 1
pares= 0
impares= 0
acum_pares=0
acum_impares=0

while i<5:
    numero = int(input("Ingrese un número entero: "))
    if (numero % 2 ==0):
        acum_pares= acum_pares + numero
        pares +=1
    else:
        acum_impares= acum_impares + numero 
        impares +=1
    i += 1
print("Se ha ingresado", pares, " números pares y ", impares, "números impares. La suma de los números pares es de ", acum_pares)




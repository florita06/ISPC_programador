#Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrarel resultado dos veces.

def sumar(num1, num2, num3):
    suma_total= (num1 + num2 + num3)
    return suma_total

#Ingreso de datos
num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
num3 = int(input("Ingrese tercer número: "))

#llamado a la función e impresión por pantalla.

suma_total = sumar(num1, num2, num3)
print("La suma total es: ",suma_total)

#Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE.


def comparacion (num1, num2):
    if num1==num2:
        print("TRUE")
    else:
        print("FALSE")
    return()

num1=int(input("Ingrese primer número: "))
num2=int(input("Ingrese segundo número: "))

comparacion(num1, num2)
#Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.


def sumayresta (num1, num2):
    suma = int(num1 + num2)
    resta = int(num1 - num2)

    return (suma, resta)

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))

suma , resta = sumayresta(num1 , num2)
print( "El resultado de sumar los dos números ingresados es :", suma)
print("El resultado de restar los dos números ingresados es: ", resta)
#Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

numero1=int(input("ingrese primer número: "))
numero2=int(input("ingrese segundo número: "))
numero3=int(input("ingrese tercer número: "))

if int(numero1>numero2 and numero1>numero3 and numero1%2 ==0) :
    print("El primer número ingresado es el mayor y es par" )

elif int(numero1>numero2 and numero1>numero3 and numero1%2 ==1) :
    print("El primer número ingresado es el mayor y es impar" )

elif int(numero1<numero2 and numero2>numero3 and numero2%2==0):
    print("El segundo número ingresado es el mayor y es par")

elif int(numero1<numero2 and numero2>numero3 and numero2%2==1):
    print("El segundo número ingresado es el mayor y es impar")

elif int(numero3<numero1 and numero2>numero3 and numero3%2==0):
    print("El tercer número es el mayor y es par")
else: 
    print("El tercer número es el mayor y es impar")

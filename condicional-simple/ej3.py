#Realizar un programa que permita ingresar “f” o “m” y determinar si vota
#en mesa femenina o masculina.

variable= input("Ingrese f, m  o x según se corresponda con su género: ")

if variable=="f":
    print("Usted vota en la mesa de mujeres")
elif variable=="m":
    print("Usted vota en la mesa de hombres")
elif variable=="x":
    print("Usted vota en la mesa sin género")
else: 
    print("El dato ingresado no es válido")

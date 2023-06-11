#Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.

lado1= float(input("Ingrese lado 1: ",))
lado2= float(input("Ingrese lado 2: ",))
lado3= float(input("Ingrese lado 3: ",))

if (lado1==lado2 and lado2==lado3):
    print("El triángulo es equilátero")
elif (lado1==lado2!=lado3 or lado1!=lado2==lado3 or lado1==lado3!=lado2):
    print("El triángulo es isóseles")
else:
    print("El triángulo es escaleno")
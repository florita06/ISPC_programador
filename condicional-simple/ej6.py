#Realice un programa donde el usuario ingrese su edad. Si es mayor de
#16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad= int(input("Ingrese su edad: ",))

if edad<16:
    print("Usted no vota")
elif edad>15 and edad<71:
    print("Puede votar")
elif edad<70 and edad<105:
    print("usted puede votar pero no es oligatorio.")
else:
    print("Usted es inmortal")
    
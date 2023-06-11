#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y 
#que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

moneda_elegida= int(input("Bienvenidos al sistema de cambio de dinero. \n Señale 1 si desea cambiar de pesos a dolares.  \n Señale 2 si desea cambiar de dolares a pesos. \n Ingrese opción: ",))

if moneda_elegida==1:
    print("Usted desea cambiar pesos a dolares. ")
elif moneda_elegida==2:
    print("Usted desea cambiar de dolares a pesos.  ")
else:
    print("No ha seleccionado ninguna de las opciones establecidas para poder operar. Ingrese un opción correcta")  

monto= float(input("Ingrese el monto  de dinero a cambiar: ",))

if moneda_elegida ==1:
    print("Usted recibe", monto/500, "dolares")
else:
    print("Usted recibe", monto*500, "pesos")
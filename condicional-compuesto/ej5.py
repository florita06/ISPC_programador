#Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

variable= int(input("Ingrese un número del 1 al 12 para saber su correspondencia con los meses del año: "))

if variable==1:
    print("El número ingresado corresponde al mes de Enero.")

elif variable==2:
    print("El número ingresado corresponde al mes de Febrero.")

elif variable==3:
    print("El número ingresado corresponde al mes de Marzo.")

elif variable==4:
    print("El número ingresado corresponde al mes de Abril.")

elif variable==5:
    print("El número ingresado corresponde al mes de Mayo.")

elif variable==6:
    print("El número ingresado corresponde al mes de Junio.")

elif variable==7:
    print("El número ingresado corresponde al mes de Julio.")

elif variable==8:
    print("El número ingresado corresponde al mes de Agosto.")

elif variable==9:
    print("El número ingresado corresponde al mes de Septiembre.")

elif variable==10:
    print("El número ingresado corresponde al mes de Octubre.")

elif variable==11:
    print("El número ingresado corresponde al mes de Noviembre.")

elif variable==12:
    print("El número ingresado corresponde al mes de Diciembre.")

else:
    print("El número ingresado no corresponde. Por favor ingrese un número de 1 a 12.")
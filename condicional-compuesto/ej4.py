#Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

variable= int(input("Ingrese un número del 1 al 7: "))

if variable==1:
    print("El número ingresado corresponde al día lunes.")

elif variable==2:
    print("El número ingresado corresponde al día martes.")

elif variable==3:
    print("El número ingresado corresponde al día miércoles.")

elif variable==4:
    print("El número ingresado corresponde al día jueves.")

elif variable==5:
    print("El número ingresado corresponde al día viernes.")

elif variable==6:
    print("El número ingresado corresponde al día sábado.")

elif variable==7:
    print("El número ingresado corresponde al día domingo.")

else:
    print("El número ingresao no corresponde. Por favor ingrese un número del 1 al 7.")
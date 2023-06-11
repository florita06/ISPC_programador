#Realice un programa que le permita al usuario simular el pago
#ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.

importe_inicial= float(input("Ingrese el importe: ",))
forma_pago= int(input("ingrese 1 para pago contado,2 para pago con tarjeta o 3 para pago con débito: "))
diez_porciento= float(importe_inicial*0.10)
cinco_porciento=  float(importe_inicial*0.05)

if forma_pago==1:
    print("Usted recibe un descuento de ", diez_porciento, " pesos. El total a abonar es ", importe_inicial-diez_porciento)

elif forma_pago==2:
    print("Usted debe pagar un recargo de", diez_porciento, " pesos . El total a abonar es ", importe_inicial+diez_porciento)

elif forma_pago==3:
    print("Usted recibe un descuento de ", cinco_porciento, " pesos. El total a abonar es ", importe_inicial-cinco_porciento)

else:
    print("Usted ha ingresado una opción incorrecta. Vuelva a intentarlo")
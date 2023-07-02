#Realice un programa que contenga una función que se llame “conversion”, que la misma contenga tres parámetros. Se pide convertir los segundos ingresados en horas, minutos y segundos
#funcion

def conversion (segundos):
   horas = segundos // 3600
   segundos_restantes = segundos % 3600
   minutos = segundos_restantes // 60
   segundos_finales = minutos % 60
   return horas, minutos, segundos_finales

    
#ingreso de datos
segundos= int(input("Ingrese la cantidad de segundos: "))

#llamar a la funcion
(horas, minutos, segundos_finales) =conversion (segundos)
print("Usted ingreso un total de:", segundos, "segundos convertidos a horas, minutos y segundos quedarían :", horas, "horas ", minutos, "minutos", segundos_finales, "segundos")


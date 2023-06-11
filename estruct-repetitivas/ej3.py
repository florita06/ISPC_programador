#Ingresar las edades y el sexo de 15 personas y determinar cuántas son
#mujeres, cuántos varones, cuántos mayores de edad y cuántos
#menores de edad

contador = 1
cant_mujeres = int()
cant_varones = int()
cant_mayores_edad = int()
cant_menores_edad = int()

while contador <=15:
    print("Persona N°: ", contador)
    sexo = input("Ingrese su sexo (M para mujer, V para varón : ",)
    edad= int(input("Ingrese su edad :" ,))
    if (sexo =="M") or (sexo == "m"):
        cant_mujeres += 1
    elif (sexo =="V") or (sexo == "v"):
        cant_varones += 1

    if edad >=18:    
        cant_mayores_edad +=1
    else:
        cant_menores_edad +=1
    
    contador += 1

print("La cantidad de mujeres son: ", cant_mujeres)
print("La cantidad de varones son: ", cant_varones)
print("La cantidad de personas mayores de edad son :" , cant_mayores_edad)
print("La cantidad de personas menores de edad son: ", cant_menores_edad)

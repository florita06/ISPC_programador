#Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección


def saludo():
    print("Hola Aula N°", aula, "¿Qué tal?" )
    print("Buenos días, todo bien")
    print("Aula ", aula, "¿Usted está aprendiendo a programar?")
    print("Aprendiendo es una forma de decir, intentando comprender.")
    print("Paciencia Aula ", aula, "de a poco todo se puede.")

    return 

aula= input("Ingrese el número de Aula que pertenece: ")
saludo()



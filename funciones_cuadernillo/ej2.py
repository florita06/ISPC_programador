def saludar(nombre1, nombre2, nombre3):
    print("Hola ", nombre1, "¿Qué tal?")
    print("Hola ", nombre2, "¿Qué tal?")
    print("Hola ", nombre3, "¿Qué tal?")
    
    return nombre1, nombre2, nombre3
nombre1 = input("Ingrese el primer nombre para recibir un saludo: ")
nombre2 = input("Ingrese el segundo nombre para recibir un saludo: ")
nombre3 = input("Ingrese el tercer nombre para recibir un saludo: ")
saludar(nombre1, nombre2, nombre3)
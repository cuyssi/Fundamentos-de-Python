# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.
#    - Guarda el contacto en una lista como un diccionario.

# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo

# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir

lista = []

while True:
    option = input(
        "¿Qué quieres hacer? (1. Añadir contacto, 2. Ver contactos, 3. Buscar por nombre, 4. Salir): ")

    if option == "1":
        nombre = input("¿Cuál es tu nombre? ")
        edad = input("¿Cuál es tu edad? ")
        ciudad = input("¿Cuál es tu ciudad? ")

        usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
        lista.append(usuario)

    elif option == "2":
        for usuario in lista:
            print("Usuario: " + usuario["nombre"] + " - " + "Edad: " + usuario["edad"] + " - " + "Ciudad: " + usuario["ciudad"])

    elif option == "3":
        busca_nombre = input("¿Qué nombre quieres buscar?: ")
        for element in lista:
            if busca_nombre == element["nombre"]:
                print("Usuario: " + element["nombre"] + " - " + "Edad: " + element["edad"] + " - " + "Ciudad: " + element["ciudad"])
                break
        else:
            print("Usuario no encontrado :( ")
    elif option == "4":
        print("Adiós!")
        break

    else:
        print("Opcion incorrecta :( ")

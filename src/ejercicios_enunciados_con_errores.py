import csv
import random


# 🧪 Ejercicios – Consola + Buenas Prácticas (KISS, DRY, Excepciones)

# Ejercicio 1: Sistema de votaciones
# -----------------------------------
# Crea un programa en consola con las siguientes opciones:
# 1. Añadir película
# 2. Votar por una película
# 3. Mostrar resultados
# 4. Salir
# Si se intenta votar por una película no registrada, muestra error
# (usa try/except con KeyError).
# Usa funciones separadas por funcionalidad.
# (Bonus: guardar votos en un fichero CSV)


# ---- esta parte del CSV es puro chatgpt, sorry :...)

films = {}

def readVotesCSV(nombre_archivo="votos.csv"):
    try:
        with open(nombre_archivo, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nombre = fila["nombre"]
                votos = int(fila["votos"])
                films[nombre] = votos
    except FileNotFoundError:
        pass

readVotesCSV()

def options():
    return """\033[92m
1. Añadir película
2. Votar por una película
3. Mostrar resultados
4. Salir
\033[0m \033[94mQué quieres hacer? Elige una opción: \033[0m"""

def addFilm():
    try:
        response = input("\033[94mIntroduce el título de la película que quieres añadir: \033[0m")
        name = response.lower()
        if name in films:
            raise ValueError("\033[91mAtención!\033[0m \033[93mEsa película ya está registrada, añade otra ;)\033[0m")
        else:
            films[name] = 0
            print(f"Película \033[93m{name}\033[0m añadida")
    except ValueError as e:
        print(e)

def voteFilm():
    try:
        response = input("\033[92mIntroduce el título de la película por la que quieres votar: \033[0m")
        name = response.lower()
        films[name] += 1
        print(f"Has votado por \033[94m{name}\033[0m")
    except KeyError:
        print("\033[91mAtención!\033[0m \033[92mNo se encuentra esa película\033[0m")

def showResult():
    if len(films) == 0:
        print("\033[91mAtención!\033[0m \033[92mAún no hay películas que mostrar\033[0m")
    else:
        for film in films:
            print(f"La película \033[94m{film}\033[0m tiene \033[94m{films[film]}\033[0m votos")

def safeVotesCSV(lista_peliculas, nombre_archivo="votos.csv"):
    with open(
        nombre_archivo, mode="w", newline="", encoding="utf-8"
    ) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "votos"])
        for nombre, num_votos in lista_peliculas.items():
            escritor.writerow([nombre, num_votos])


def menu(options):
    while True:
        option = input(options())

        if option == "1":
            addFilm()
        if option == "2":
            voteFilm()
        if option == "3":
            showResult()
        if option == "4":
            safeVotesCSV(films)
            print("\033[91mHasta pronto!\033[0m")
            break

menu(options)


# Ejercicio 2: Limpieza de datos crudos
# -------------------------------------
# Dada una lista de nombres con errores (espacios, mayúsculas, duplicados),
# crea una función que la limpie devolviendo una lista ordenada
# y sin duplicados.
# Todos los nombres deben tener solo la primera letra en mayúscula.
# Muestra cuántos nombres únicos hay.
# 💡 Añade manejo de errores si algún elemento no es una cadena
# (TypeError o AttributeError)


names = ["ana", "Juan", "maria ", "Ana", " Juan", 999]


def clear(list):
    correctNames = []
    for name in names:
        try:
            correctName = name.strip().capitalize()
            correctNames.append(correctName)
        except (AttributeError, TypeError):
            print(f"\033[91mAtención!\033[0m \033[94m{name}\033[0m No es una cadena de texto")
    namesInOrden = set(correctNames)
    print(f"\033[94m{namesInOrden}\033[0m")


clear(names)

# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.


def countWords(string):
    count = len(string)
    print(f"Hay \033[94m{count}\033[0m palabras")

def countWordFrequency(string):
    word = {}
    for element in string:
        if element not in word:
            word[element] = 1
        else:
            word[element] += 1
    print(f"\033[94m{word}\033[0m")

def getMostFrequentWord(string):
    list = {}
    word = ""
    for element in string:
        if element not in list:
            list[element] = 1
        else:
            list[element] += 1
        if element > word:
            word = element
    print(f"La palabra \033[94m{word}\033[0m es la que mas veces se repite porque aparece \033[94m{list[word]}\033[0m veces")

def analyzeText(string):
    try:
        words = string.lower().split()
        if len(words) == 0:
            raise ValueError("\033[91mAtención!\033[0m \033[93mIntroduce un texto, por favor\033[0m")
        countWords(words)
        countWordFrequency(words)
        getMostFrequentWord(words)
    except ValueError as e:
        print(e)

text = input("\033[92mIngresa aquí un texto:\033[0m ")
analyzeText(text)


# Ejercicio 4: Simulador de inventario
# -------------------------------------
# Crea un sistema que permita gestionar productos en un inventario.
# Cada producto tiene nombre, stock y precio.
# Opciones:
# 1. Añadir producto
# 2. Actualizar stock
# 3. Eliminar producto
# 4. Ver inventario
# 💡 Usa try/except para validar entradas numéricas y para controlar si el
#  producto no existe.


inventory = []


def showMenu():

    return """\033[92m\033[4m
    Elige una opción:\033[0m \033[92m
    1. Añadir producto
    2. Actualizar stock
    3. Eliminar producto
    4. Ver inventario
    5. Salir\033[0m
    \033[94mOpcion:\033[0m """

def findProduct(name):
    for product in inventory:
        if product["name"] == name:
            return product
    return None


def addProduct():
    try:
        name = input("\033[94mQué producto quieres añadir:\033[0m ")
        if not name:
            raise ValueError("\033[91mAtención!\033[0mIntroduce un producto")

        if findProduct(name):
            raise ValueError("\033[91mAtención!\033[0mEste producto ya está registrado, introduce uno nuevo")
            return
        else:
            stock = input("\033[94mCuántas unidades?:\033[0m ")
            price = input("\033[94mCuánto cuesta?:\033[0m ")
            product = {
                "name": name,
                "stock": stock,
                "price": price
            }
            print(f"Producto \033[93m{product["name"]}\033[0m añadido")
            return inventory.append(product)
    except ValueError as e:
        print(e)

def updateInventory():
    try:
        name = input("\033[94mQué stock quieres modificar?Elige un producto:\033[0m ")
        product = findProduct(name)

        if product is None:
            raise ValueError("\033[91mAtención!\033[0mEse producto no está registrado :(")
        else:

            newValue = input("\033[94mIntroduce el nuevo valor:\033[0m ")
            product["stock"] = newValue
            print(f"Stock de \033[93m{product["name"]}\033[0m modificado")
    except ValueError as e:
        print(e)


def showInventory():
    try:
        if len(inventory) == 0:
            raise ValueError("\033[91mAtención!\033[0m No hay productos en el inventario aún.")
        else:
            print(f"\033[93m{inventory}\033[0m")
    except ValueError as e:
        print(e)


def deleteProduct():
    try:
        name = input("\033[94mQué producto quieres eliminar?:\033[0m ")
        product = findProduct(name)
        if product is None:
            raise ValueError("\033[91mAtención!\033[0m Ese producto no está registrado :(")
        else:
            inventory.remove(product)
            print(f"Producto \033[93m{product["name"]}\033[0m eliminado")
    except ValueError as e:
        print(e)


while True:
    try:
        option = input(showMenu())
        if option:

            if option == "1":
                addProduct()
            elif option == "2":
                updateInventory()
            elif option == "3":
                deleteProduct()
            elif option == "4":
                showInventory()
            elif option == "5":
                print("\033[91mHasta pronto!\033[0m")
                break
        else:
            raise ValueError("\033[91mAtención!\033[0mIntroduce una opción")
    except ValueError as e:
        print(e)


# # Ejercicio 5: Generador de alias seguro
# # ---------------------------------------
# # Pide al usuario nombre y apellido, y genera un alias así:
# # - 3 letras del apellido (mayúsculas)
# # - 2 letras del nombre (minúsculas)
# # - número aleatorio del 10 al 99
# # - símbolo especial aleatorio
# # 💡 Valida que el nombre y apellido tengan longitud suficiente (ValueError)


def lettersFirstName(string):
    fullName = string.lower().split()
    name = fullName[0]
    if len(name) >= 3:
        lettersName = name[0] + name[1]
    else:
        raise ValueError("\033[91mAtención!\033[0mIntroduce un nombre con al menos 3 carácteres")
    return lettersName

def lettersLastName(string):
    fullName = string.upper().split()
    firtsName = fullName[1]
    if len(firtsName) >= 3:
        lettersLastName = firtsName[0] + firtsName[1] + firtsName[2]
    else:
        raise ValueError("\033[91mAtención!\033[0mIntroduce un apellido con al menos 3 carácteres")
    return lettersLastName

def randomNumber():
    num = random.randint(10, 99)
    return num

def randomSimbol():
    sim = random.choice("!@#~$%&¬/?¿'¡")
    return sim

def aliasGenerator():
    response = input("\033[94mIntroduce tu nombre y tu primer apellido:\033[0m ")
    name = lettersFirstName(response)
    lastName = lettersLastName(response)
    number = randomNumber()
    simbol = randomSimbol()
    alias = lastName + name + str(number) + str(simbol)
    print(alias)

aliasGenerator()


# Ejercicio 6: Comprobador de contraseñas seguras
# ------------------------------------------------
# Pide una contraseña al usuario.
# Valida que:
# - Tiene al menos 8 caracteres
# - Contiene mayúsculas, minúsculas y números
# 💡 Usa raise y excepciones personalizadas con mensajes explicativos.

def moreThan8(string):
    if len(string) < 8:
        raise ValueError("\033[91mAtención!\033[0m \033[93mLa contraseña debe contener al menos 8 caracteres.\033[0m")
    return True

def haveUpper(string):
    if not any(c.isupper() for c in string):
        raise ValueError("\033[91mAtención!\033[0m \033[93mLa contraseña debe contener al menos una mayúscula.\033[0m")
    return True

def haveLower(string):
    if not any(c.islower() for c in string):
        raise ValueError("\033[91mAtención!\033[0m \033[93mLa contraseña debe contener al menos una minúscula.\033[0m")
    return True

def haveNumber(string):
    if not any(c.isdigit() for c in string):
        raise ValueError("\033[91mAtención!\033[0m \033[93mLa contraseña debe contener al menos un número.\033[0m")
    return True


def validation():
    while True:
        try:
            password = input("\033[94mIntroduce tu contraseña:\033[0m ")
            moreThan8(password)
            haveUpper(password)
            haveLower(password)
            haveNumber(password)
            print("\033[92mContraseña correcta\033[0m, ¡Bienvenido!")
            break
        except ValueError as e:
            print(e)


validation()


# 🌟 Reto Extra: Simulador de reservas de hotel
# ----------------------------------------------
# Habitaciones del 101 al 110. El usuario puede:
# 1. Ver habitaciones disponibles
# 2. Reservar habitación (introduciendo su nombre)
# 3. Cancelar reserva
# 4. Ver reservas confirmadas
# 5. Salir
# Las reservas se almacenan en un diccionario {habitacion: nombre}
# Usa funciones y control de errores con KeyError si la habitación no existe.
# (Bonus: mostrar mapa visual, reservas múltiples, carga inicial aleatoria)

def showMenu():
    return """\033[92m
    1.Ver habitaciones disponibles
    2.Reservar habitación
    3.Cancelar reserva
    4.Ver reservas confirmadas
    5.Ver estado de las habitaciones
    6.Salir\033[0m
    \033[94mQué quieres hacer?:\033[0m """

roomFree = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
rooms = {}
states = {}

def initial():
    name = random.choice(["Joaquin", "Marcos", "Ana"])
    room = random.choice(roomFree)
    roomFree.remove(room)
    rooms[room] = name
    states[room] = "Ocupada"

initial()

def showRoom():
    try:
        if len(roomFree) > 0:
            print(f"\033[93mHabitaciones libres:\033[0m {roomFree}")
        else:
            raise ValueError("\033[91mAtención!\033[0m \033[93mNo hay habitaciones disponibles :(\033[0m")
    except ValueError as e:
        print(e)

def reserveRoom():
    try:
        if len(roomFree) > 0:
            name = input("\033[94mA qué nombre quiere reservar la habitación?:\033[0m ")
            room = roomFree.pop(0)
            states[room] = "Ocupada"
            rooms[room] = name
            print(f"\033[93mSu habitación {room} ha sido reservada ;)\033[0m")
        else:
            raise ValueError("\033[91mAtención!\033[0m \033[93mNo hay habitaciones disponibles :(\033[0m")
    except ValueError as e:
        print(e)

def cancelRoom():
    try:
        room = int(input("\033[94mCuál es el número de la habitacion de la reserva que quiere cancelar?:\033[0m "))
        del rooms[room]
        roomFree.insert(0, room)
        print("\033[93mReserva cancelada ;)\033[0m")
    except KeyError:
        print("\033[91mAtención!\033[0m Número de habitacion no valido")

def roomsState():
    for room in roomFree:
        states[room] = "Libre"
    for room in states:
        print(f"\033[93mLa habitación {room}:\033[0m está \033[94m{states[room]}\033[0m")

def gestionHotel():
    while True:
        option = input(showMenu())
        if option == "1":
            showRoom()
        elif option == "2":
            reserveRoom()
        elif option == "3":
            cancelRoom()
        elif option == "4":
            print(rooms)
        elif option == "5":
            roomsState()
        elif option == "6":
            break

gestionHotel()

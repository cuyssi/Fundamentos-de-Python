# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.

lista = ["pan", "leche", "harina", "agua", "lechuga"]
print(lista[0])
print(lista[-1])

# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.

lista.append("naranjas")
lista.remove("leche")

print(lista)


# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.

lista = [5, 8, 9, 1, 7, 3, 2, 4, 6]
lista.sort()

print(lista)

# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

coordenadas = (40.4168, -3.7038)
print(coordenadas)

# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.

elementos = ("elemento1", "elemento2", "elemento3")
elementos2 = "elemento4"

print(elementos)

# No cambia porque las tuplas son inmutables

# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

diccionario = {"nombre": "Ana", "edad": 44, "ciudad": "Avilés"}

print(diccionario)

# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.

diccionario["ciudad"] = "Gijón"
diccionario["email"] = "cuyssi@hotmail.com"

print(diccionario)

# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta..

for element in diccionario.items():
    print(element)


# ------------------------------
# SETS
# ------------------------------

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.

lista = ["ana", "lore", "angel", "nico", "lore", "nico", "angel"]
lista2 = set(lista)

print(lista2)

# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 3]

nole = set(lista1) - set(lista2)
print(nole)


# ------------------------------
# EXTRA
# ------------------------------

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.

diccionario = {"angel": ["ver anime"], "lore": ["aprender idiomas"], "nico": ["juagar al pc"]}

diccionario["angel"].append("jugar pc")

print(diccionario)

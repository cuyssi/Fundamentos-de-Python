# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type() para imprimir qué tipo de dato es cada una:
a = "Hola"
b = 25
c = 3.14
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"

toInt = int("42") + 8
print(toInt)

toStr = str(100)
print("Tu puntuación final es: " + toStr)

# ------------------------------
# VARIABLES
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.

nombre = "Marta"
edad = 30
print("Hola, soy " + nombre + " y tengo " + str(edad) + " años.")

# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
x = "gato"
y = "perro"
# Intercambia sus valores para que x valga "perro" y y valga "gato".

x, y = y, x

print("x es " + x)
print("y es " + y)


# ------------------------------
# OPERADORES
# ------------------------------

# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:

pan = 1.50
leche = 1.24
huevos = 2.70

# Calcula el total y muestra: “El total de tu compra es de: 4,25€”

print("El total de tu compra es de : " + str(pan + leche + huevos) + "€")


# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.

if int(input("Dime un número: ")) % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------

# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.

if int(input("¿Cuántos años tienes? ")) >= 18:
    print("Puedes entrar :)")
else:
    print("Acceso denegado!!")


# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.

opcion = input("Elige una opción (1.Ver perfil, 2.Editar perfil o 3.Cerrar sesión): ")

if opcion == "1":
    print("Has elegido: Ver perfil")

elif opcion == "2":
    print("Has elegido: Editar perfil")

elif opcion == "3":
    print("Has elegido: Cerrar sesión")
else:
    print("Opción no válida")


# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------

# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().

sorpresa = input("Escribe cualquier cosa: ")

try:
    int(sorpresa)
    print("Has escrito un número entero")

except ValueError:
    try:
        float(sorpresa)
        print("Has escrito un número decimal")

    except ValueError:
        if sorpresa == "":
            print("No has escrito nada :(")
        else:
            print("Parece que es una cadena de texto")


# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.

numero1 = int(input("Dame un numero: "))
numero2 = int(input("Dame otro numero: "))
eleccion = input("Elige una opcion: (1.Sumar, 2.Restar, 3.Multiplicar, 4.Dividir)")

if eleccion == "1":
    print(numero1 + numero2)
elif eleccion == "2":
    print(numero1 - numero2)
elif eleccion == "3":
    print(numero1 * numero2)
elif eleccion == "4":
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        print(numero1 / numero2)

# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”

edad = int(input("¿Cuántos años tienes? "))

if edad < 3:
    print("Bebé")
elif edad >= 3 and edad <= 12:
    print("Infancia")
elif edad >= 13 and edad <= 17:
    print("Adolescencia")
elif edad >= 18 and edad <= 64:
    print("Adulto")
elif edad >= 100:
    print("Senior")

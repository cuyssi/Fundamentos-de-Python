# 🧪 Fundamentos Python III – Funciones

# ------------------------------
# ✨ Ejercicio 1: Saludo básico
# Objetivo: Aprender a definir y llamar funciones
# Crea una función llamada saludar() que imprima: "¡Hola, bienvenido/a!"
# Luego llama a la función una vez para comprobar que funciona.

def saludar():
    print("¡Hola, bienvenido/a!")

saludar()
# ------------------------------
# ✨ Ejercicio 2: Saludo personalizado
# Objetivo: Trabajar con parámetros
# Crea una función llamada saludar_persona(nombre) que imprima: "Hola, [nombre]!"
# Llama a la función dos veces con diferentes nombres.

def saludar_persona(nombre):
    print("Hola, " + nombre + "!")

saludar_persona("Ana")
saludar_persona("Marcos")

# ------------------------------
# ✨ Ejercicio 3: Suma fácil
# Objetivo: Usar parámetros y return
# Crea una función llamada sumar(a, b) que devuelva la suma de dos números.
# Guarda el resultado en una variable y muéstralo con print().

suma = 0

def sumar(a, b):
    suma = a + b
    print(suma)

sumar(2, 3)


# ------------------------------
# ✨ Ejercicio 4: ¿Par o impar?
# Objetivo: Usar lógica dentro de una función
# Escribe una función es_par(numero) que devuelva True si el número es par y False si es impar.
# Pruébala con varios números y muestra el resultado.

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(isEven(4))
print(isEven(5))

# ------------------------------
# ✨ Ejercicio 5: Mensaje con formato
# Objetivo: Devolver una cadena con formato
# Crea una función llamada mensaje(nombre, edad) que devuelva una frase como:
# "Me llamo Marta y tengo 30 años."
# Usa return y luego muestra el mensaje con print().

def mensaje(nombre, edad):
    return ("Me llamo " + nombre + " y tengo " + str(edad) + " años.")

print(mensaje("Ana", 44))

# ------------------------------
# ✨ Ejercicio 6: Calculadora simple
# Objetivo: Practicar varias funciones juntas
# Crea 4 funciones: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
# Llama a cada una con un par de números y muestra los resultados.
# Bonus: en dividir(), si el segundo número es 0, devuelve "No se puede dividir por cero"

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return ("No se puede dividir por 0")
    else:
        return a / b

print(sumar(6, 3))
print(restar(6, 3))
print(multiplicar(6, 3))
print(dividir(6, 0))
print(dividir(6, 3))

# ------------------------------
# ✨ Ejercicio 7: Edad en el futuro
# Objetivo: Usar return con operaciones
# Escribe una función llamada edad_futura(edad_actual, años) que calcule la edad que tendrás después de X años.

def edad_futura(edad_actual, años):
    return edad_actual + años

print(edad_futura(44, 25))

# ------------------------------
# ✨ Ejercicio 8: Media de 3 números
# Objetivo: Trabajar con números y return
# Crea una función llamada calcular_media(a, b, c) que devuelva la media de tres números.
# Prueba la función y muestra el resultado con print().

def calcular_media(a, b, c):
    return ((a + b + c) / 3)

print(calcular_media(1, 2, 3))

# ------------------------------
# ✨ Ejercicio 9: Mostrar menú (sin lógica)
# Objetivo: Separar la presentación de la lógica
# Escribe una función llamada mostrar_menu() que imprima un pequeño menú como:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión


def mostrar_menu():
    print("1. Ver perfil\n2. Editar perfil\n3. Cerrar sesión")

mostrar_menu()


# ------------------------------
# 🌟 Reto Final: Generador de contraseñas

# Crea una función llamada generar_contraseña(longitud)
# que devuelva una contraseña aleatoria con la longitud especificada.

# La contraseña debe contener una mezcla de:
# - letras minúsculas (a-z)
# - letras mayúsculas (A-Z)
# - números (0-9)
# - símbolos como !, @, #, $, %, &, *

# Ejemplo de uso:
# contraseña = generar_contraseña(12)
# print(contraseña)  # -> A2c$e9#Tq&7L

# Bonus:
# - Usa la librería random
# - Controla que la longitud mínima sea 8 caracteres
# - Añade un mensaje de advertencia si se pide menos de 8

import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        return ("Por favor, ingresa un valor mas alto que 8")
    else:
        letras = string.ascii_letters + string.digits + "!@#$%&*"
        pwd = ''.join(random.choice(letras) for i in range(longitud))
        return pwd

contraseña = generar_contraseña(9)
print(contraseña)

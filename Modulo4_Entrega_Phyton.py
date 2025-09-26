# %%
# 1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_letras(cadena):
    cadena = cadena.lower()
    frecuencias = {}
    
    for letra in cadena:
        if letra != " ":  # ignorar espacios
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    
    return frecuencias

texto = "Me llamo Pilar y soy de Zaragoza"
frecuencias = contar_letras(texto)

# Imprimir con formato diccionario
for letra, valor in frecuencias.items():
    print(f'({letra} ---> {valor})')

# %%
# 2.Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
lista=[1,2,3,4,6,7,19,34]

def doble_valor(numero): 
    """
    Args:
    numeros(lista): lista de numeros
    Returns:
    lista: lista de numeros multiplicados por dos
    """
    return numero*2


resultado = list(map(doble_valor, lista))
print(resultado)


# %%
# 3.Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def devolver_palabra_objetivo(objetivo,lista_palabras):
    """"
    Args:
    objetivo(str): palabra que tiene que aparecer en la lista de palabras
    Returns:
    str: palabras que contienen la palabra objetivo
    """
    lista_palabras_objetivo=[]
    for palabra in lista_palabras:
        if objetivo in palabra:
            lista_palabras_objetivo.append(palabra)
    return lista_palabras_objetivo

lista_palabras=["perro","gato","pajaro","avestruz","leon","araña"]
resultado=devolver_palabra_objetivo("ar", lista_palabras)
print(resultado)



# %%
# 4.Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def restar(x,y):
    return x-y

def diferencia_valores(lista1,lista2):
    """Args: 
    lista 1(lista): lista 1 de valores
    lista 2(lista): lista 2 de valores
    Returns:
    lista: lista que muestra la diferencia entre las dos listas
    """
    return list(map(restar,lista1,lista2))

lista1=[55,47,43,23,56,21]
lista2=[3,6,8,4,5,3]

resultado=diferencia_valores(lista1,lista2)
print(resultado)

# %%
 # 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def funcion(lista_numeros, nota_aprobado=5):
    """
    Args:
        lista_numeros (list): lista de numeros
        nota_aprobado (float): nota de aprobado
    Returns:
        tuple: (media, estado)
    """
    media = sum(lista_numeros) / len(lista_numeros)
    if media >= nota_aprobado:
        estado = "Aprobado"
    else:
        estado = "Suspenso"
    return (media, estado)

# Lista de ejemplo
lista_numeros = [2, 4, 7, 9, 3, 4]
resultado = funcion(lista_numeros)
print(resultado)




# %%
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(numero):
    """
    Calcula el factorial de un número de manera recursiva.
    Args:
        numero (int): número para calcular factorial
    Returns:
        int: factorial de numero
    """
    if numero <= 1:       
        return 1
    else:                 
        return numero * factorial(numero - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(resultado)


# %%
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def convertidor(lista):
    """
    Args:
        lista (list): lista de tuplas a convertir a string
    Returns:
        list: lista de strings
    """
    return list(map(str, lista))

# Ejemplo de uso
lista_tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = convertidor(lista_tuplas)
print(resultado)


# %%
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:
    numero1 = float(input("Dime un número aleatorio: "))
    numero2 = float(input("Dime otro número aleatorio: "))
    resultado = numero1 / numero2
except ValueError:
    print("Error: Debes introducir solo números")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
else:
    print(f"El resultado de la división es {resultado}")


# %%
# 9.Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def es_valida(mascota, lista_excluir):
    return mascota not in lista_excluir

def funcion_eliminar(lista1, lista2):
    """
    Args:
        lista1 (list): lista principal con todas las mascotas
        lista2 (list): lista secundaria con mascotas a eliminar
    Returns:
        list: lista de mascotas sin tener en cuenta las que hay que eliminar
    """
    def filtro(mascota):
        return es_valida(mascota, lista2)

    return list(filter(filtro, lista1))


lista_mascotas = ["Perro", "Gato", "Serpiente Pitón", "Cocodrilo", "Oso", "Mapache", "Tigre"]
lista_mascotas_excluir = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

resultado = funcion_eliminar(lista_mascotas, lista_mascotas_excluir)
print(resultado)


# %%
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def media(lista_numeros):
    if not lista_numeros:
        raise ListaVaciaError("La lista está vacía, no se puede calcular la media")
    return sum(lista_numeros) / len(lista_numeros)
# %%
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.

try:
    edad = int(input("Introduzca su edad: "))
    if edad < 0 or edad > 120:
        print("Edad fuera de rango (0-120)")
    else:
        print(f"Tu edad es {edad}")
except ValueError:
    print("Has introducido un valor no numérico")



# %%
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función

def lista_longitud(frase):
    """
    Args:
        frase (str): frase de palabras
    Returns:
        list: lista con la longitud de cada palabra
    """
    palabras = frase.split()
    return list(map(len, palabras))  # Aplicamos len a cada palabra

# Ejemplo de uso
frase = "Hola mi nombre es Pilar"
resultado = lista_longitud(frase)
print(resultado)


# %%
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayus_minus_unicas(conjunto):
    """
    Args:
        conjunto (str): conjunto de caracteres
    Returns:
        list: lista de tuplas con (mayúscula, minúscula) sin repeticiones
    """
    # Convertimos a conjunto para eliminar duplicados
    caracteres_unicos = set(conjunto)
    
    # Función que devuelve tupla (mayúscula, minúscula)
    def mayus_minus(c):
        return (c.upper(), c.lower())
    
    # Usamos map sobre los caracteres únicos
    return list(map(mayus_minus, caracteres_unicos))

# Ejemplo de uso
conjunto = "aAbBcCaa"
resultado = mayus_minus_unicas(conjunto)
print(resultado)


# %%
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función

def palabras_por_letra(lista_palabras, letra):
    """
    Retorna las palabras que comienzan con la letra especificada.
    
    Args:
        lista_palabras (list): Lista de palabras.
        letra (str): Letra con la que deben comenzar las palabras.
        
    Returns:
        list: Palabras que comienzan con la letra indicada.
    """
    # Convertir la letra a minúscula para comparación insensible a mayúsculas
    letra = letra.lower()
    
    # Usamos filter para seleccionar las palabras que comienzan con la letra
    resultado = list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras))
    return resultado

palabras = ["manzana", "Melón", "pera", "mango", "banana"]
print(palabras_por_letra(palabras, "m"))





# %%
# 15. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_con_letra(lista_palabras, letra):
    """
    Args:
        lista_palabras (list): lista de palabras
        letra (str): letra con la que deben comenzar las palabras
    Returns:
        list: lista de palabras que comienzan con la letra indicada
    """
    # Función que verifica si una palabra empieza con la letra

    def empieza_con(palabra):
        return palabra.lower().startswith(letra.lower())
    return list(filter(empieza_con, lista_palabras))


        


# %%
#16.Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mayores_n(texto, n):
    """
    Args: 
        texto (str): Cadena de texto
        n (int): Número mínimo de letras que deben tener las palabras
    Returns:
        list: Lista de las palabras del texto que tengan más de n letras
    """
    palabras = texto.split()  # separar el texto en palabras
    
    def es_larga(palabra):
        return len(palabra) > n
    
    return list(filter(es_larga, palabras))


# Ejemplo de uso
texto = "Me llamo Pilar y estoy aprendiendo Python"
resultado = palabras_mayores_n(texto, 4)
print(resultado) 



# %%
# 17.Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    """
    Args:
        digitos (list): lista de dígitos (enteros entre 0-9)
    Returns:
        int: número formado por los dígitos
    """
    return reduce(lambda x, y: x * 10 + y, digitos)


lista = [5, 6, 2,7]
resultado = lista_a_numero(lista)
print(resultado)


# %%
# 18.Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "Pilar", "edad": 21, "calificacion": 92},
    {"nombre": "Jorge", "edad": 23, "calificacion": 85}
]


def aprobado(estudiante):
    return estudiante["calificacion"] >= 90


estudiantes_aprobados = list(filter(aprobado, estudiantes))


print(estudiantes_aprobados)


# %%
# 19. Crea una función lambda que filtre los números impares de una lista dada.

# Lista de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filtrar números impares usando lambda y filter
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)


# %%
# 20.Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

# Lista de ejemplo con enteros y strings
lista_mixta = [1, "hola", 3, "mundo", 5, "Python", 7]

# Filtrar solo los enteros
solo_enteros = list(filter(lambda x: isinstance(x, int), lista_mixta))

print(solo_enteros)


# %%
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

# Función lambda que calcula el cubo
cubo = lambda x: x**3

# Ejemplo de uso
numero = 4
resultado = cubo(numero)
print(resultado)


# %%
# 22.Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

# Lista de ejemplo
numeros = [2, 3, 4, 5]

# Función reduce para calcular el producto total
producto_total = reduce(lambda x, y: x * y, numeros)

print(producto_total)


# %%
# 23.Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

# Lista de palabras de ejemplo
palabras = ["Hola", "mundo", "esto", "es", "Python"]

# Usamos reduce para concatenar todas las palabras
frase = reduce(lambda x, y: x + " " + y, palabras)

print(frase)


# %%
# 24.Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

# Lista de ejemplo
numeros = [100, 20, 5]

# Usamos reduce para calcular la diferencia total
diferencia_total = reduce(lambda x, y: x - y, numeros)

print(diferencia_total)


# %%
# 25.Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    """
    Args:
        cadena (str): cadena de texto a analizar
    Returns:
        int: número de caracteres en la cadena
    """
    return len(cadena)

# Ejemplo de uso
texto = "Hola mundo"
print(contar_caracteres(texto))


# %%
# 26.Crea una función lambda que calcule el resto de la división entre dos números dados.

# Función lambda para calcular el resto de la división
resto = lambda x, y: x % y

# Ejemplo de uso
a = 17
b = 5
resultado = resto(a, b)
print(resultado)


# %%
# 27.Crea una función que calcule el promedio de una lista de números

def promedio(lista_numeros):
    """
    Args:
        lista_numeros (list): lista de números
    Returns:
        float: promedio de la lista
    """
    if not lista_numeros:
        return 0  # o puedes lanzar una excepción si quieres
    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo de uso
numeros = [4, 5, 6, 7]
resultado = promedio(numeros)
print(resultado)


# %%
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    """
    Args:
        lista (list): lista de elementos
    Returns:
        elemento: primer elemento duplicado encontrado o None si no hay duplicados
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # si no hay duplicados

# Ejemplo de uso
lista = [3, 5, 2, 4, 5, 7, 2]
resultado = primer_duplicado(lista)
print(resultado)



# %%
# 29.Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(valor):
    """
    Args:
        valor: cualquier tipo de dato (int, float, str, etc.)
    Returns:
        str: cadena enmascarada con '#' excepto los últimos 4 caracteres
    """
    texto = str(valor)  # Convertimos a string
    if len(texto) <= 4:
        return texto  # Si tiene 4 o menos caracteres, no se enmascara
    return '#' * (len(texto) - 4) + texto[-4:]

# Ejemplo de uso
numero = 123456789
resultado = enmascarar_variable(numero)
print(resultado)


# %%
# 30.Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    """
    Args:
        palabra1 (str): primera palabra
        palabra2 (str): segunda palabra
    Returns:
        bool: True si son anagramas, False si no
    """
    # Eliminamos espacios y convertimos a minúsculas para comparar correctamente
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Comparamos si las letras ordenadas son iguales
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
resultado = son_anagramas("roma", "amor")
print(resultado)  # True

resultado2 = son_anagramas("hola", "mundo")
print(resultado2)  # False


# %%
# 31.Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def lista_nombres():
    """
    Solicita al usuario una lista de nombres y un nombre a buscar.
    Si el nombre está en la lista, imprime un mensaje, de lo contrario lanza una excepción.
    """
  
    lista = input("Dame una lista de nombres separados por comas: ").split(",")

    lista = [nombre.strip() for nombre in lista]

    nombre = input("¿Qué nombre quieres buscar en esta lista?: ").strip()

    if nombre in lista:
        print(f'El nombre "{nombre}" fue encontrado')
    else:
        raise Exception(f' El nombre "{nombre}" no fue encontrado')


lista_nombres()


# %%
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre_completo, empleados):
    """
    Args:
        nombre_completo (str): Nombre completo del empleado a buscar.
        empleados (list): Lista de diccionarios con 'nombre' y 'puesto'.
    
    Returns:
        str: El puesto del empleado si se encuentra, o un mensaje indicando que no trabaja aquí.
    """
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return f'{empleado["nombre"]} trabaja como {empleado["puesto"]}'
    return f'La persona "{nombre_completo}" no trabaja aquí.'


# Ejemplo de uso
empleados = [
    {"nombre": "Pilar Samper", "puesto": "Data Analyst"},
    {"nombre": "Juan Pérez", "puesto": "Ingeniero"},
    {"nombre": "Ana López", "puesto": "Diseñadora"}
]

print(buscar_empleado("Pilar Samper", empleados))
print(buscar_empleado("Luis García", empleados))





# %%
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# Listas de ejemplo
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]

# Usando lambda + map para sumar elemento por elemento
suma_listas = list(map(lambda x, y: x + y, lista1, lista2))

print(suma_listas)


# %%
# 34.Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol. Código a seguir: 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas. 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad. 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas. 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes. 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
class Arbol:
    def __init__(self):
        # 1. Inicializar tronco y ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # 2. Aumentar longitud del tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # 3. Agregar una rama nueva de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # 4. Aumentar en 1 la longitud de todas las ramas
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # 5. Eliminar una rama por índice (si existe)
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida: no hay rama en ese índice.")

    def info_arbol(self):
        # Información general del árbol
        return f"Tronco: {self.tronco}, Ramas: {self.ramas}"


# %%
# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. Código a seguir:  Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante  Implementar el método True y False . retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.  Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.  Implementar el método agregar_dinero para agregar dinero al saldo del usuario. Caso de uso: Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. 2 PROYECTO LÓGICA Katas de PythonAgregar 20 unidades de saldo de "Bob". Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".  Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        """
        Inicializa un usuario con nombre, saldo y si tiene cuenta corriente.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """
        Retira dinero del saldo si es posible.
        Lanza un error si no tiene suficiente saldo o no tiene cuenta corriente.
        """
        if not self.cuenta_corriente:
            raise Exception(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise Exception(f"{self.nombre} no tiene suficiente saldo.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transfiere dinero desde otro usuario al usuario actual.
        Lanza un error si no es posible.
        """
        if not otro_usuario.cuenta_corriente:
            raise Exception(f"{otro_usuario.nombre} no tiene cuenta corriente.")
        if cantidad > otro_usuario.saldo:
            raise Exception(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} transfirió {cantidad} a {self.nombre}.")
        print(f"Saldo {otro_usuario.nombre}: {otro_usuario.saldo}, Saldo {self.nombre}: {self.saldo}")

    def agregar_dinero(self, cantidad):
        """
        Agrega dinero al saldo.
        """
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")
# Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 1. Agregar 20 unidades a Bob
bob.agregar_dinero(20)  # Saldo Bob: 70

# 2. Transferir 80 unidades desde Bob a Alicia
alicia.transferir_dinero(bob, 80)  # Bob -> Alicia

# 3. Retirar 50 unidades de Alicia
alicia.retirar_dinero(50)  # Saldo Alicia actualizado


# %%
#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , procesar_texto . contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función Código a seguir: Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario. Crear una función reemplazar_palabras para remplazar una que devolver el texto con el remplazo de palabras. Crear una función palabra_original del texto por una palabra_nueva . Tiene eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada. Caso de uso: Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra en el texto.
    Devuelve un diccionario {palabra: frecuencia}.
    """
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra del texto por otra.
    """
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    """
    Elimina todas las apariciones de una palabra en el texto.
    """
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción indicada:
    - "contar": cuenta las palabras
    - "reemplazar": reemplaza una palabra por otra
    - "eliminar": elimina una palabra
    
    Args:
        texto (str): texto de entrada
        opcion (str): opción a aplicar ("contar", "reemplazar", "eliminar")
        args: argumen
         """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("La opción 'reemplazar' requiere dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("La opción 'eliminar' requiere un argumento: palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

texto = "el perro corre rápido y el perro ladra fuerte"

# Contar palabras
print(procesar_texto(texto, "contar"))

# Reemplazar palabra
print(procesar_texto(texto, "reemplazar", "perro", "gato"))

# Eliminar palabra
print(procesar_texto(texto, "eliminar", "perro"))



# %%
# 38.Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def determinar_momento_del_dia(hora):
    """
    Determina si es de mañana, tarde o noche según la hora.
    
    Args:
        hora (int): Hora en formato 24h (0-23)
        
    Returns:
        str: "Mañana", "Tarde" o "Noche"
    """
    if 6 <= hora < 12:
        return "Mañana"
    elif 12 <= hora < 20:
        return "Tarde"
    elif 0 <= hora < 6 or 20 <= hora <= 23:
        return "Noche"
    else:
        return "Hora no válida"

# Solicitar la hora al usuario
try:
    hora_usuario = int(input("Introduce la hora actual (0-23): "))
    resultado = determinar_momento_del_dia(hora_usuario)
    print(f"Es {resultado}.")
except ValueError:
    print("Por favor, introduce un número válido entre 0 y 23.")




# %%
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:  0  69 insuficiente  70  79 bien  80  89 muy bien  90  100 excelente
def calificacion_texto(nota):
    """
    Convierte una calificación numérica en texto según las reglas:
    0-69: insuficiente
    70-79: bien
    80-89: muy bien
    90-100: excelente
    """
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación no válida"

# Solicitar calificación al usuario
try:
    nota_usuario = float(input("Introduce la calificación del alumno (0-100): "))
    print(f"Calificación en texto: {calificacion_texto(nota_usuario)}")
except ValueError:
    print("Por favor, introduce un número válido.")




# %%
# 40.Escribe una función que tome dos parámetros: "triangulo" ) y figura (una cadena que puede ser "rectangulo" , "circulo" o datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    """
    Calcula el área de una figura según el tipo indicado.
    
    Args:
        figura (str): "triangulo", "rectangulo" o "circulo"
        datos (tuple): datos necesarios para el cálculo
            - triangulo: (base, altura)
            - rectangulo: (ancho, alto)
            - circulo: (radio,)
    
    Returns:
        float: área de la figura
    """
    if figura.lower() == "triangulo":
        base, altura = datos
        return 0.5 * base * altura
    elif figura.lower() == "rectangulo":
        ancho, alto = datos
        return ancho * alto
    elif figura.lower() == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    else:
        raise ValueError("Figura no válida. Usa 'triangulo', 'rectangulo' o 'circulo'.")

# Ejemplos de uso
print("Área del triángulo:", calcular_area("triangulo", (5, 10)))
print("Área del rectángulo:", calcular_area("rectangulo", (4, 8)))
print("Área del círculo:", calcular_area("circulo", (3,)))


# %%
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: 1. Solicita al usuario que ingrese el precio original de un artículo. 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

# Solicitar precio original
try:
    precio_original = float(input("Introduce el precio original del artículo: "))
    
    if precio_original < 0:
        print("El precio no puede ser negativo.")
    else:
        # Preguntar si tiene cupón de descuento
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        
        if tiene_cupon == "sí" or tiene_cupon == "si":
            # Solicitar valor del cupón
            descuento = float(input("Introduce el valor del cupón de descuento: "))
            if descuento > 0:
                precio_final = precio_original - descuento
                # Asegurarse de que el precio final no sea negativo
                if precio_final < 0:
                    precio_final = 0
                print(f"Precio final con descuento: {precio_final:.2f}€")
            else:
                print("El valor del cupón no es válido. No se aplica descuento.")
                print(f"Precio final: {precio_original:.2f}€")
        elif tiene_cupon == "no":
            print(f"No hay descuento aplicado. Precio final: {precio_original:.2f}€")
        else:
            print("Respuesta no válida. Por favor, responde sí o no.")
except ValueError:
    print("Por favor, introduce un número válido para el precio y el descuento.")


# %%




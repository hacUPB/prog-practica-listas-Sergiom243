# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz():
    import numpy as np

    matriz1 = np.array([[1, 2]])
    matriz2 = np.array([[3, 4]])

    matriz_suma = matriz1 + matriz2

    resultado_escalar = np.sum(matriz_suma)

    print("El resultado escalar es:", resultado_escalar)

    import numpy as np

    matriz1 = np.array([[0, 0]])
    matriz2 = np.array([[0, 0]])

    matriz_suma = matriz1 + matriz2

    resultado_escalar = np.sum(matriz_suma)

    print("El resultado escalar es:", resultado_escalar)

    import numpy as np

    matriz1 = np.array([[-1, -2]])
    matriz2 = np.array([[-3, -4]])

    matriz_suma = matriz1 + matriz2

    resultado_escalar = np.sum(matriz_suma)

    print("El resultado escalar es:", resultado_escalar)


# Ejercicio 2: Encontrar el valor máximo en una matriz
import numpy as np

def maximo_matriz(matriz):

    matriz = np.array([[1, 2], [3, 4]])

    numero_max = np.max(matriz)

    print ("el numero max es: ", numero_max)
    
    import numpy as np





# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

try:
    numero = int(input("Ingresa un número: "))
    
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")


# Ejercicio 4: Transponer una matriz

matriz_original = [
    [1, 2],
    [3, 4]
]

print("Matriz original:")
for fila in matriz_original:
    print(fila)

def transponer_matriz(matriz):
    transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
    return transpuesta

matriz_transpuesta = transponer_matriz(matriz_original)

print("\nMatriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]

numeros_pares = filtrar_pares(lista_numeros)

print("Lista original:", lista_numeros)
print("Números pares:", numeros_pares)

# Ejercicio 6: Contar la cantidad de palabras en una frase
frase = "Hola, cómo estás hoy?"

def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

numero_palabras = contar_palabras(frase)

print(f"Frase: '{frase}'")
print(f"Número de palabras: {numero_palabras}")


# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(Número):
    Número = int(input("Por favor ingrese un número: "))

    for i in range (1, 11):
        multiplicación = Número * i
        print(f" {Número} x {i} = {multiplicación}")
        
tabla_multiplicar(numero)



# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    return len([num for num in lista if num < 0])

lista_numeros = [-1, 0, 1, 2, -3]

numero_negativos = contar_negativos(lista_numeros)

print("Lista:", lista_numeros)
print(f"Cantidad de números negativos: {numero_negativos}")


# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    return lista == sorted(lista)

lista_numeros = [1, 2, 4, 5] 

resultado = lista_ordenada(lista_numeros)


print(f"Lista: {lista_numeros}")
print(f"¿Está ordenada de menor a mayor?: {resultado}")


# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for caracter in texto:
        
        if caracter.isupper():
            texto_cifrado += chr((ord(caracter) + desplazamiento - 65) % 26 + 65)
       
        elif caracter.islower():
            texto_cifrado += chr((ord(caracter) + desplazamiento - 97) % 26 + 97)

        else:
            texto_cifrado += caracter

    return texto_cifrado

texto = input("Introduce el texto o frase a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento: "))

texto_cifrado = cifrado_cesar(texto, desplazamiento)

print(f"Texto cifrado: {texto_cifrado}")

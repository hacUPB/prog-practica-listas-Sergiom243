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
def contar_palabras(frase):
    """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    pass

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    pass

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
    pass

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    pass

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto:str, desplazamiento:int):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()
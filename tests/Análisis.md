Le pedimos al usuario ingresar una letra o más dependiendo en si el usuario elige o no, si elige no seguir ingresando letras, estas letras pasan a una cadena de caracteres y el usuario elige un número de cambio para esta letra la cual se va a mantener en un rango entre 97 y 122 los cuales corresponden a el abecedario en minúsculas de la tabla ASCII si elige otro número y este número es mayor a el rango de lista como 125 este se le resta el rango máximo y se suma al rango mínimo para que siga dentro de la lista.

al hacer el cambio, este número resultante se va a cambiar de número a letra según la tabla.

# Pseudocódigo

def cifrado_cesar (texto:str, desplazamiento:int)

texto = print(input("por favor ingrese una oración o texto"))
texto_nuevo = ""

for letra in cadena:
    texto_nuevo += "letra"
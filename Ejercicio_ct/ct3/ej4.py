""" Ejercicio 4 """
"""
Buscador de letras: 
Para este ejercicio usted tomará de base la palabra "Anticonstitucionalidad".
Se le dará un mensaje indicando cuál es la palabra a utilizar (indicado en la indicacion anterior)^.
Se le pedirá al usuario ingresar un caracter, el cual será buscado dentro de la palabra ya mencionada.
Por medio de un mensaje indicará en qué posición se encuentra el la primera coincidencia de la letra buscada.
Ejemplo:
    - "Ingrese una letra a buscar" : c
    - "La letra buscada es: c, y ha sido encontrada en la posicion 4".
"""
name = "Anticonstitucionalidad"
buscar = input("Ingrese una letra: ")
posicion = name.index(buscar)
#[0, 1 , 2, 3, 4...] -- indices
#[M E L I S A]

print(f"La letra buscada es: {buscar} y ha sido encontrada en la posicion {posicion}")



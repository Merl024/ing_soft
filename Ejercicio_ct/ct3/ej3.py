""" Ejercicio 3 """
"""
Elaborará un primer intento de ahorcado.
Primero, se le pedirá al usuario (como si fueran usuarios dsitintos) ingresar una palabra.
Segundo, se le pedirá al usuario ingresar una letra.
Al final, se le mostrarán al usuario los siguientes resultados:
    - "La palabra ingresada es X, la cual contiene Y caracteres".
    - "De sus 3 intentos ha hacertado en Z ocasiones, y la cantidad de coincidencias es de W"
        (número de veces que encontró las letras dentro de la palabra)
Ejemplo:
    - "La palabra ingresada es Destornillador, la cual contiene 14 caracteres".
    // Supongamos que las letras ingresadas fueron L, U, O
    - "De sus 3 intentos ha hacertado en 2 ocasiones, y la cantidad de coincidencias es de 4"
    // L se encontró 2 veces, U no se encontró y O fue encontrada 2 veces.
Esto implica que debe buscar las letras independientemente de ser mayúsculas o minúsculas.
"""
#Le pedimos al usuario que ingrese la palabra para el juego
usuario1 = input('Ingresa una palabra de su preferencia: ').lower()

# El ej. pide que ingresemos 3 letras, asi que, por separado, guardamos en variables las letras que se quieren buscar.
letra1= input('Ingrese una letra: ').lower()
letra2 = input('Ingrese una letra: ').lower()
letra3 = input('Ingrese una letra: ').lower()

#El .count() sirve para buscar cuantas veces una elemento se repite dentro a una variables
#En este caso, queremos saber cuantas veces esta la letra 1 en usuario, y se guarda en una variable para procesarla
coincidencia1 = usuario1.count(letra1)
coincidencia2 = usuario1.count(letra2)
coincidencia3 = usuario1.count(letra3)

#Lo pasado es para registras las coincidencias por letra, esta es para las coincidencias totales
ocaciones = coincidencia1 + coincidencia2 + coincidencia3

print(f'La palabra ingresada es {usuario1.capitalize()} la cual contiene {len(usuario1)} caracteres.')
print(f'De sus 3 intentos ha acertado en {ocaciones}')
print(f'{letra1.upper()} se encontró {coincidencia1} veces, {letra2.upper()} se encontró {coincidencia2} y {letra3.upper()} fue encontrada {coincidencia3} veces.')
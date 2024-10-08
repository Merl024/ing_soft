""" Ejercicio 5 """
"""
Calculador de notas: 
Primero, pedirá al usuario ingresar su nombre y luego su apellido.
Segundo, pedirá al usuario ingresar las notas de sus evaluaciones.
Serán cuatro evaluaciones, identificadas como Nota1, Nota2, Nota3 y Nota4.
Cada una de estas notas tiene una ponderación de 10%, 20%, 30% y 40%.
Al final, le devolverá un mensaje indicando su nombre y el resultado de su nota final
según las ponderaciones que ya se indicó para estas notas.
Nota. Con las herramientas con las que contamos, vamos a asumir:
    - El usuario sabe que debe ingresar valores entre 0 y 10
    - El usuario puede ingresar valores decimales para cada una de las notas.
Ejemplo:
    - "Hola Alvin Portillo (20000059), tu nota final es de 7.3".
"""
name = input('Ingrese su nombre completo: ').capitalize()
carnet = int(input('Ingrese su numero de carnet: '))            

nota1 = float(input('Ingrese su primera nota: '))
nota2 = float(input('Ingrese su segunda nota: '))
nota3 = float(input('Ingrese su tercera nota: '))
nota4 = float(input('Ingrese su cuarta nota: '))

calculo1 = nota1 * 0.1
calculo2 = nota2 * 0.2
calculo3 = nota3 * 0.3
calculo4 = nota4 * 0.4

notaFinal = calculo1 + calculo2 + calculo3 + calculo4

print(f'Hola, {name} ({carnet}). Su nota final es: {notaFinal:.2f}')
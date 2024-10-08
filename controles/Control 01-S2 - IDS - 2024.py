### Control 01 - Introducción al Desarrollo de Software - 2024 ###

"""Para el presente control se le pide que escriba el código debajo de cada pregunta a la cual 
está dando respuesta.
Los temas a evaluar son:
* La declaración y asignación de variables
* Variables de los tipos (Int, Str, Float y bool)
* Impresión de resultados en pantalla, con y sin formato

CONSIDERACIONES ESPECIALES:
*UTILIZAR LOS CONCEPTOS VISTOS EN CLASE (NO INPUTS, NO IF, NO LIBRERIAS, ETC.)"""

#################################
# 1. Cálculo de notas # 15 puntos
#################################
"""
Por medio de variables, crear un algoritmo que capture los siguientes datos:
* Numero de carnet del alumno
* Nombre del alumno
* Apellido del alumno
* Notas (Instancias: 9.9, 7.85, 4.99)
* Ponderaciones (Instancias: 25%, 35%, 40%)
* Imprimir en un solo mensaje los datos del alumno, la nota final (1 decimal) y una indicación
  de TRUE/FALSE si el alumno ha aprobado, si sabe que la nota mínima para aprobar es de 7.0
"""

#Datos del alumno
carnetAlumno = 20245324
nameAlumno = 'Melisa'
apellidoAlumno = 'Rivas'

#Notas del estudiante
nota1 = 9.9
nota2 = 7.85
nota3 = 4.99

#Ponderaciones de las notas
ponderacion1 = 25/100
ponderacion2 = 35/100
poonderacion3 = 40/100

#Verificando si aprobo o no
notaFinal = (nota1*ponderacion1) + (nota2*ponderacion2) + (nota3 * poonderacion3)
aprobar = notaFinal > 7.0

#Imprimiendo
print(f'1. El estudiante de carnet {carnetAlumno}, cuyo nombre es {nameAlumno} {apellidoAlumno}. Tuvo una nota final de {notaFinal:.1f}. ¿Aprobo la materia? {aprobar}')

#####################################
# 2. Conversor de monedas # 10 puntos
#####################################
"""
Por medio de variables capturará un monto en dólares estadounidenses.
Además, sabiendo que el tipo de cambio por euro es de 0.89 y por yen es de 143.56.
Imprima un mensaje (preferiblemente legible) de tal forma que se muestre el monto en dólares
y su equivalencia euros y yenes, todos con 2 decimales. Nota, no usar símbolos de monedas, solo nombres.
(Instancia: dolares 1,234.56)
"""
montoDol = 1234.56
euros = montoDol / 0.89
yen = montoDol / 143.56

print(f'2. El monto en dolares es: {montoDol:,.2f}. Esto es equivalente a {euros:,.2f} euros y {yen:.2f} yenes')

##########################################
# 3. Crecimiento de una planta # 15 puntos
##########################################
"""
Imagina que queremos simular el crecimiento de una planta durante 5 días. 
Cada día, la planta crece una cierta cantidad de centímetros, pero esta cantidad aumenta ligeramente en 
comparación con el día anterior debido a que la planta se hace más fuerte.
Suponiendo que la planta inicialmente mide 18.23 centimetros 
y cada día crece un 5% (tamaño actual * (1+5%)),
presentar una serie de mensajes en pentalla desde el tamaño inicial hasta el final,
el último mensaje debe indicar algo como:
"La plantita el dia uno medía 18.23 y al final de 5 días mide 23.27 cms"
"""
#Datos
inicial = 18.23
crecimiento = 5/100

#Crecimiento por 5 dias
dia1 = inicial * (1+crecimiento)
dia2 = dia1 * (1+crecimiento)
dia3 = dia2 * (1+crecimiento)
dia4 = dia3 * (1+crecimiento)
dia5 = dia4 * (1+crecimiento)

print(f'3. La plantita el día uno medía {inicial} y al final de 5 días mide {dia5:.2f}')
